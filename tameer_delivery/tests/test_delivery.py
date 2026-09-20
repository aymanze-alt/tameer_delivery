import frappe
import frappe.utils

from frappe.tests.utils import FrappeTestCase

from tameer_delivery import api as delivery_api


class TestDelivery(FrappeTestCase):
	def setUp(self):
		frappe.set_user("Administrator")
		self.ensure_role_and_custom_fields()
		self.driver = self.make_user("delivery_driver@example.com", ["Driver"])
		self.outsider = self.make_user("delivery_outsider@example.com", ["Customer"])
		self.shipment, self.customer = self.make_shipment(self.driver)

	def tearDown(self):
		frappe.db.rollback()
		frappe.set_user("Administrator")

	def ensure_role_and_custom_fields(self):
		if not frappe.db.exists("Role", "Driver"):
			role = frappe.new_doc("Role")
			role.role_name = "Driver"
			role.desk_access = 0
			role.save(ignore_permissions=True)
		for fname, (ftype, opts, insert_after) in {
			"tc_delivery_driver": ("Link", "User", "total_weight"),
			"tc_delivery_status": ("Select", "Not Delivered\nIn Transit\nDelivered\nFailed", "tc_delivery_driver"),
			"tc_delivery_proof": ("Link", "Delivery Proof", "tc_delivery_status"),
		}.items():
			if not frappe.db.exists("Custom Field", {"dt": "Shipment", "fieldname": fname}):
				frappe.get_doc({
					"doctype": "Custom Field",
					"dt": "Shipment",
					"fieldname": fname,
					"fieldtype": ftype,
					"options": opts,
					"insert_after": insert_after,
				}).insert(ignore_permissions=True)
		frappe.db.commit()

	def ensure_masters(self):
		if not frappe.db.exists("Customer Group", "All Customer Groups"):
			frappe.get_doc({
				"doctype": "Customer Group",
				"customer_group_name": "All Customer Groups",
				"is_group": 0,
			}).insert(ignore_permissions=True, ignore_mandatory=True)
		if not frappe.db.exists("Territory", "All Territories"):
			frappe.get_doc({
				"doctype": "Territory",
				"territory_name": "All Territories",
				"is_group": 0,
			}).insert(ignore_permissions=True, ignore_mandatory=True)
		frappe.db.commit()

	def make_user(self, email, roles):
		if frappe.db.exists("User", email):
			user = frappe.get_doc("User", email)
		else:
			user = frappe.get_doc({
				"doctype": "User",
				"email": email,
				"first_name": email.split("@")[0].replace("_", " ").title(),
				"send_welcome_email": 0,
			})
			user.insert(ignore_permissions=True)
		user.add_roles(*roles)
		frappe.db.commit()
		return email

	def make_shipment(self, driver):
		self.ensure_masters()
		customer = None
		existing = frappe.get_all(
			"Customer", filters={"customer_name": "_Test Delivery Customer"}, limit=1
		)
		if existing:
			customer = existing[0].name
		else:
			customer = frappe.get_doc({
				"doctype": "Customer",
				"customer_name": "_Test Delivery Customer",
				"customer_group": "All Customer Groups",
				"territory": "All Territories",
			}).insert(ignore_permissions=True).name
		frappe.db.commit()

		pickup_address = frappe.get_doc({
			"doctype": "Address",
			"address_title": "Warehouse A",
			"address_line1": "1 Pickup Street",
			"city": "Riyadh",
			"country": "Saudi Arabia",
		}).insert(ignore_permissions=True).name
		delivery_address = frappe.get_doc({
			"doctype": "Address",
			"address_title": "Test Delivery Customer",
			"address_line1": "123 Test Street",
			"city": "Riyadh",
			"country": "Saudi Arabia",
			"links": [{"link_doctype": "Customer", "link_name": customer}],
		}).insert(ignore_permissions=True).name

		shipment = frappe.get_doc({
			"doctype": "Shipment",
			"shipment_type": "Goods",
			"pickup_from_type": "Company",
			"pickup_company": frappe.defaults.get_defaults().company or "Wind Power LLC",
			"pickup": "Warehouse A",
			"pickup_address_name": pickup_address,
			"pickup_date": frappe.utils.today(),
			"pickup_from": "09:00:00",
			"pickup_to": "17:00:00",
			"delivery_to_type": "Customer",
			"delivery_customer": customer,
			"delivery_to": "_Test Delivery Customer",
			"delivery_address": "123 Test Street, Riyadh",
			"delivery_address_name": delivery_address,
			"description_of_content": "Furniture",
			"value_of_goods": 250,
			"tc_delivery_driver": driver,
			"tc_delivery_status": "Not Delivered",
			"shipment_parcel": [
				{"length": 30, "width": 20, "height": 15, "weight": 5, "count": 2, "description_of_content": "Furniture"}
			],
		}).insert(ignore_permissions=True)
		shipment.submit()
		frappe.db.commit()
		return shipment.name, customer

	def test_driver_sees_assigned_shipment(self):
		frappe.set_user(self.driver)
		shipments = delivery_api.get_assigned_shipments()
		names = [s["name"] for s in shipments]
		self.assertIn(self.shipment, names)

	def test_outsider_cannot_view_list(self):
		frappe.set_user(self.outsider)
		with self.assertRaises(frappe.PermissionError):
			delivery_api.get_assigned_shipments()

	def test_submit_delivery_proof_syncs_shipment(self):
		frappe.set_user(self.driver)
		res = delivery_api.submit_delivery_proof(
			shipment=self.shipment,
			received_by="Mohammed Ali",
			delivery_status="Delivered",
			signature="/files/sig.png",
			proof_photo="/files/proof.jpg",
			latitude=24.7136,
			longitude=46.6753,
			geo_accuracy=12.5,
			remark="On time",
		)
		self.assertTrue(res["name"])

		proof = frappe.get_doc("Delivery Proof", res["name"])
		self.assertEqual(proof.shipment, self.shipment)
		self.assertEqual(proof.driver, self.driver)
		self.assertEqual(proof.received_by, "Mohammed Ali")
		self.assertEqual(round(float(proof.latitude), 4), 24.7136)
		self.assertEqual(float(proof.geo_accuracy), 12.5)

		shipment = frappe.get_doc("Shipment", self.shipment)
		self.assertEqual(shipment.tc_delivery_status, "Delivered")
		self.assertEqual(shipment.tc_delivery_proof, res["name"])
		self.assertEqual(shipment.tracking_status, "Delivered")

	def test_unassigned_driver_cannot_submit(self):
		frappe.set_user(self.outsider)
		with self.assertRaises(frappe.PermissionError):
			delivery_api.submit_delivery_proof(shipment=self.shipment, received_by="X",
											   delivery_status="Delivered")

	def test_live_location_and_tracking(self):
		frappe.set_user(self.driver)
		res = delivery_api.update_driver_location(
			latitude=24.7, longitude=46.6, accuracy=8, speed=45, device="Mobile"
		)
		self.assertTrue(res["saved"])

		frappe.set_user("Administrator")
		locs = delivery_api.get_driver_locations(minutes=15)
		self.assertTrue(any(l["driver"] == self.driver for l in locs))