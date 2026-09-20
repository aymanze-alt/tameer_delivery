import frappe

from tameer_delivery.api import is_driver, is_manager


def get_context(context):
	if frappe.session.user == "Guest":
		frappe.redirect("/login?redirect-to=/delivery")

	if not (is_driver() or is_manager()):
		frappe.throw(frappe._("This page is reserved for drivers and managers."), frappe.PermissionError)

	from frappe.sessions import get_csrf_token

	context.user_fullname = frappe.utils.get_fullname(frappe.session.user)
	context.user_email = frappe.session.user
	context.is_manager = is_manager()
	context.csrf_token = get_csrf_token()
	context.no_cache = 1
	return context