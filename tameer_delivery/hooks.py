app_name = "tameer_delivery"
app_title = "Tameer Delivery"
app_publisher = "Tameer"
app_description = "Delivery management app for drivers"
app_email = "info@tameer.local"
app_license = "mit"

# Apps
# ------------------

required_apps = ["erpnext"]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "tameer_delivery",
# 		"logo": "/assets/tameer_delivery/logo.png",
# 		"title": "Tameer Delivery",
# 		"route": "/tameer_delivery",
# 		"has_permission": "tameer_delivery.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tameer_delivery/css/tameer_delivery.css"
# app_include_js = "/assets/tameer_delivery/js/tameer_delivery.js"

# include js, css files in header of web template
# web_include_css = "/assets/tameer_delivery/css/tameer_delivery.css"
# web_include_js = "/assets/tameer_delivery/js/tameer_delivery.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tameer_delivery/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "tameer_delivery/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "tameer_delivery.utils.jinja_methods",
# 	"filters": "tameer_delivery.utils.jinja_filters"
# }

# Installation
# ------------

after_install = "tameer_delivery.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tameer_delivery.uninstall.before_uninstall"
# after_uninstall = "tameer_delivery.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "tameer_delivery.utils.before_app_install"
# after_app_install = "tameer_delivery.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "tameer_delivery.utils.before_app_uninstall"
# after_app_uninstall = "tameer_delivery.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tameer_delivery.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tameer_delivery.tasks.all"
# 	],
# 	"daily": [
# 		"tameer_delivery.tasks.daily"
# 	],
# 	"hourly": [
# 		"tameer_delivery.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tameer_delivery.tasks.weekly"
# 	],
# 	"monthly": [
# 		"tameer_delivery.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "tameer_delivery.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tameer_delivery.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tameer_delivery.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["tameer_delivery.utils.before_request"]
# after_request = ["tameer_delivery.utils.after_request"]

# Job Events
# ----------
# before_job = ["tameer_delivery.utils.before_job"]
# after_job = ["tameer_delivery.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"tameer_delivery.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

# Fixtures
# --------

fixtures = [
	{
		"dt": "Print Format",
		"filters": [["module", "=", "Tameer Delivery"]]
	},
	{
		"dt": "Workspace",
		"filters": [["module", "=", "Tameer Delivery"]]
	}
]

