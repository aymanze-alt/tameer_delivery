import frappe


CUSTOM_FIELDS = [
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


def execute():
	# ensure the Custom Field records exist (idempotent)
	for cf in CUSTOM_FIELDS:
		if frappe.db.exists("Custom Field", {"dt": cf["dt"], "fieldname": cf["fieldname"]}):
			continue
		frappe.get_doc({"doctype": "Custom Field", **cf}).insert(ignore_permissions=True)

	# make sure the physical columns exist even if the Custom Field sync was skipped
	for cf in CUSTOM_FIELDS:
		if not frappe.db.has_column(cf["dt"], cf["fieldname"]):
			frappe.db.add_column(cf["dt"], cf["fieldname"], "Data")

	frappe.db.updatedb("Shipment")
	frappe.db.commit()