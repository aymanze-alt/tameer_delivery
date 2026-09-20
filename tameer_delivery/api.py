import frappe
from frappe import _

from frappe.utils import now, flt


MANAGER_ROLES = ("Administrator", "System Manager", "Sales Manager", "Stock Manager", "Delivery Manager")


def is_driver(user=None):
	user = user or frappe.session.user
	return "Driver" in frappe.get_roles(user)


def is_manager(user=None):
	user = user or frappe.session.user
	return bool(set(frappe.get_roles(user)) & set(MANAGER_ROLES))


def _require_actor():
	if not (is_driver() or is_manager()):
		frappe.throw(_("You do not have permission to perform this action."), frappe.PermissionError)


def _shipment_query():
	"""Common filters for the shipment list shown to someone."""
	roles = frappe.get_roles()
	filters = {"docstatus": 1}
	if is_driver():
		filters["tc_delivery_driver"] = frappe.session.user
	if not is_manager() and not is_driver():
		frappe.throw(_("You do not have permission to view deliveries."), frappe.PermissionError)
	return filters


@frappe.whitelist()
def get_assigned_shipments():
	"""Shipments assigned to the logged-in driver (or all, for managers)."""
	filters = _shipment_query()
	shipments = frappe.get_all(
		"Shipment",
		filters=filters,
		fields=[
			"name", "tc_delivery_status as delivery_status", "delivery_customer",
			"delivery_to", "delivery_address", "delivery_contact",
			"pickup_date", "total_weight", "value_of_goods",
			"tc_delivery_proof as delivery_proof", "modified",
		],
		order_by="modified desc",
	)

	for s in shipments:
		s["proof"] = None
		if s.get("delivery_proof"):
			proof = frappe.db.get_value(
				"Delivery Proof", s["delivery_proof"],
				["name", "delivery_status", "received_by", "delivery_datetime"], as_dict=1
			)
			s["proof"] = proof

	return shipments


@frappe.whitelist()
def get_shipment_detail(shipment):
	"""Full detail of one shipment + any existing delivery proof."""
	shipment_doc = frappe.get_doc("Shipment", shipment)
	_permit_shipment(shipment_doc)

	parcels = []
	for p in shipment_doc.get("shipment_parcel") or []:
		parcels.append({
			"length": p.length, "width": p.width, "height": p.height,
			"weight": p.weight, "count": p.count, "description_of_content": p.description_of_content,
		})

	proof = None
	if shipment_doc.get("tc_delivery_proof"):
		p = frappe.db.get_value(
			"Delivery Proof", shipment_doc.tc_delivery_proof,
			["name", "delivery_status", "received_by", "delivery_datetime",
			 "signature", "proof_photo", "latitude", "longitude", "geo_accuracy", "remark"],
			as_dict=1
		)
		proof = p

	customer = shipment_doc.delivery_customer or ""
	contact = shipment_doc.delivery_contact or shipment_doc.delivery_contact_name or ""

	return {
		"shipment": shipment_doc.name,
		"customer": customer,
		"delivery_to": shipment_doc.delivery_to,
		"delivery_address": shipment_doc.delivery_address,
		"delivery_contact": contact,
		"delivery_contact_email": shipment_doc.delivery_contact_email,
		"delivery_status": shipment_doc.get("tc_delivery_status") or "Not Delivered",
		"delivery_driver": shipment_doc.get("tc_delivery_driver"),
		"pickup_date": shipment_doc.pickup_date,
		"value_of_goods": shipment_doc.value_of_goods,
		"total_weight": shipment_doc.total_weight,
		"parcels": parcels,
		"proof": proof,
	}


@frappe.whitelist()
def submit_delivery_proof(shipment, received_by=None, delivery_status="Delivered", signature=None,
						  proof_photo=None, latitude=None, longitude=None, geo_accuracy=None, remark=None):
	"""Create a Delivery Proof and sync the Shipment delivery status."""
	_require_actor()
	shipment_doc = frappe.get_doc("Shipment", shipment)
	_permit_shipment(shipment_doc)

	delivery_status = delivery_status or "Delivered"
	if delivery_status in ("Delivered", "Partially Delivered") and not received_by:
		frappe.throw(_("Received By is required for delivered shipments."))

	if frappe.db.exists("Delivery Proof", {"shipment": shipment, "docstatus": 0}):
		proof = frappe.get_doc("Delivery Proof", {"shipment": shipment, "docstatus": 0})
	else:
		proof = frappe.new_doc("Delivery Proof")

	proof.shipment = shipment
	proof.driver = frappe.session.user
	proof.delivery_status = delivery_status
	proof.delivery_datetime = now()
	if received_by:
		proof.received_by = received_by
	if signature:
		proof.signature = signature
	if proof_photo:
		proof.proof_photo = proof_photo
	if latitude is not None:
		proof.latitude = flt(latitude)
	if longitude is not None:
		proof.longitude = flt(longitude)
	if geo_accuracy is not None:
		proof.geo_accuracy = flt(geo_accuracy)
	if remark:
		proof.remark = remark
	proof.save(ignore_permissions=True)

	_sync_shipment_status(shipment, proof.name, delivery_status)

	return {
		"name": proof.name,
		"delivery_status": proof.delivery_status,
		"delivery_datetime": proof.delivery_datetime,
	}


def _sync_shipment_status(shipment, proof_name, delivery_status):
	tracking_map = {
		"Delivered": "Delivered",
		"Partially Delivered": "In Progress",
		"Failed": "In Progress",
	}
	frappe.db.set_value("Shipment", shipment, {
		"tc_delivery_status": delivery_status,
		"tc_delivery_proof": proof_name,
		"tracking_status": tracking_map.get(delivery_status, "In Progress"),
	}, update_modified=True)


@frappe.whitelist()
def update_driver_location(latitude, longitude, accuracy=None, speed=None, heading=None, device=None):
	"""Live GPS ping from the driver's mobile page (throttled to reduce noise)."""
	_require_actor()

	latitude = flt(latitude)
	longitude = flt(longitude)

	last = frappe.db.get_value(
		"Driver Location Log",
		{"driver": frappe.session.user},
		["ping_time", "latitude", "longitude"],
		order_by="creation desc"
	)
	if last:
		from frappe.utils.data import time_diff_in_seconds
		age = time_diff_in_seconds(now(), last[0])
		moved = abs(latitude - flt(last[1])) + abs(longitude - flt(last[2]))
		if age < 10 and moved < 0.00005:
			return {"saved": False, "reason": "throttled"}

	log = frappe.new_doc("Driver Location Log")
	log.driver = frappe.session.user
	log.latitude = latitude
	log.longitude = longitude
	log.accuracy = flt(accuracy) if accuracy is not None else None
	log.speed = flt(speed) if speed is not None else None
	log.heading = flt(heading) if heading is not None else None
	log.source = "Web"
	log.device = (device or "")[:200]
	log.ping_time = now()
	log.save(ignore_permissions=True)
	frappe.db.commit()

	return {"saved": True, "ping_time": log.ping_time}


@frappe.whitelist()
def get_driver_locations(minutes=15):
	"""Latest ping per active driver — used by the tracking map."""
	if not is_manager():
		frappe.throw(_("Only managers can view the live map."), frappe.PermissionError)

	minutes = int(minutes) or 15
	since = frappe.utils.add_to_date(now(), minutes=-minutes)
	from frappe.utils.data import time_diff_in_seconds

	logs = frappe.db.sql("""
		SELECT driver, user.first_name, user.full_name, l.latitude, l.longitude,
		       l.accuracy, l.speed, l.ping_time
		FROM `tabDriver Location Log` l
		INNER JOIN `tabUser` user ON user.name = l.driver
		WHERE l.ping_time >= %s
		AND l.creation = (
			SELECT MAX(l2.creation) FROM `tabDriver Location Log` l2
			WHERE l2.driver = l.driver AND l2.ping_time >= %s
		)
	""", (since, since), as_dict=1)

	result = []
	for row in logs:
		row["age_seconds"] = int(time_diff_in_seconds(now(), row["ping_time"]))
		row["current_shipment"] = _driver_current_shipment(row["driver"])
		result.append(row)

	return result


def _driver_current_shipment(driver):
	return frappe.db.get_value(
		"Shipment",
		{"tc_delivery_driver": driver, "tc_delivery_status": ["in", ["In Transit", "Not Delivered"]]},
		["name", "delivery_customer", "delivery_address"],
		order_by="modified desc"
	) or None


def _permit_shipment(shipment_doc):
	"""Drivers can only touch shipments assigned to them."""
	if is_manager():
		return
	if not is_driver():
		frappe.throw(_("You do not have permission to view this shipment."), frappe.PermissionError)
	assigned = shipment_doc.get("tc_delivery_driver")
	if assigned and assigned != frappe.session.user:
		frappe.throw(_("This shipment is assigned to another driver."), frappe.PermissionError)