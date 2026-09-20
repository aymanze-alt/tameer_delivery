import frappe

from tameer_delivery.api import is_manager


def get_context(context):
	if frappe.session.user == "Guest":
		frappe.redirect("/login?redirect-to=/delivery_tracking")

	if not is_manager():
		frappe.throw(frappe._("Only managers can view the live tracking map."), frappe.PermissionError)

	from frappe.sessions import get_csrf_token

	context.user_fullname = frappe.utils.get_fullname(frappe.session.user)
	context.csrf_token = get_csrf_token()
	context.no_cache = 1
	return context