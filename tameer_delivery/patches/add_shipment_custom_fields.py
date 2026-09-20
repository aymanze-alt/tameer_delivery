import frappe


def execute():
	custom_fields = [
		{
			"dt": "Shipment",
			"fieldname": "tc_delivery_driver",
			"fieldtype": "Link",
			"insert_after": "total_weight",
			"label": "Delivery Driver",
			"no_copy": 1,
			"options": "User",
			"search_index": 1,
		},
		{
			"dt": "Shipment",
			"fieldname": "tc_delivery_status",
			"fieldtype": "Select",
			"default": "Not Delivered",
			"insert_after": "tc_delivery_driver",
			"label": "Delivery Status",
			"no_copy": 1,
			"options": "Not Delivered\nIn Transit\nDelivered\nFailed",
		},
		{
			"dt": "Shipment",
			"fieldname": "tc_delivery_proof",
			"fieldtype": "Link",
			"insert_after": "tc_delivery_status",
			"label": "Delivery Proof",
			"no_copy": 1,
			"options": "Delivery Proof",
			"read_only": 1,
		},
	]

	for cf in custom_fields:
		if frappe.db.exists("Custom Field", {"dt": cf["dt"], "fieldname": cf["fieldname"]}):
			continue
		frappe.get_doc({"doctype": "Custom Field", **cf}).insert(ignore_permissions=True)

	frappe.db.commit()