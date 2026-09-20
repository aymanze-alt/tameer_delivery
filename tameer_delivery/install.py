import frappe


def after_install():
	create_driver_role()


def create_driver_role():
	if not frappe.db.exists("Role", "Driver"):
		role = frappe.new_doc("Role")
		role.role_name = "Driver"
		role.desk_access = 0
		role.disabled = 0
		role.save(ignore_permissions=True)
		frappe.db.commit()