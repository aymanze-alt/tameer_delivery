import frappe
from frappe.model.document import Document


class DeliveryProof(Document):
	def before_validate(self):
		if not self.driver:
			self.driver = frappe.session.user
		if not self.delivery_datetime:
			self.delivery_datetime = frappe.utils.now()

		if not self.customer and self.shipment:
			shipment = frappe.get_doc("Shipment", self.shipment)
			self.customer = shipment.delivery_customer or ""
			self.delivery_address = shipment.delivery_address or ""

	def validate(self):
		if self.latitude and self.longitude:
			self.location_preview = f"https://maps.google.com/?q={self.latitude},{self.longitude}"

	def on_update(self):
		# keep the Shipment delivery status in sync
		if self.shipment:
			frappe.db.set_value("Shipment", self.shipment, "tc_delivery_status", self.delivery_status, update_modified=False)

	def on_trash(self):
		if self.shipment:
			frappe.db.set_value("Shipment", self.shipment, "tc_delivery_status", "Not Delivered", update_modified=False)