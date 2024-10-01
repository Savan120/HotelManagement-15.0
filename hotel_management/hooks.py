app_name = "hotel_management"
app_title = "Hotel Management"
app_publisher = "Savan"
app_description = "This is use for hotel related operations."
app_email = "patelsavan6891@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "hotel_management",
# 		"logo": "/assets/hotel_management/logo.png",
# 		"title": "Hotel Management",
# 		"route": "/hotel_management",
# 		"has_permission": "hotel_management.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hotel_management/css/hotel_management.css"
# app_include_js = "/assets/hotel_management/js/hotel_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/hotel_management/css/hotel_management.css"
# web_include_js = "/assets/hotel_management/js/hotel_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hotel_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Customer" : "public/js/Customer_get_age.js"}	
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "hotel_management/public/icons.svg"

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
# 	"methods": "hotel_management.utils.jinja_methods",
# 	"filters": "hotel_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hotel_management.install.before_install"
# after_install = "hotel_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "hotel_management.uninstall.before_uninstall"
# after_uninstall = "hotel_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "hotel_management.utils.before_app_install"
# after_app_install = "hotel_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "hotel_management.utils.before_app_uninstall"
# after_app_uninstall = "hotel_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hotel_management.notifications.get_notification_config"

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

doc_events = {
    "Reservation": {
        "on_submit": "hotel_management.hotel_management.doctype.reservation.reservation.update_room_status_on_reservation",

    }
}




# Scheduled Tasks
# ---------------
# scheduler_events = {
#     "cron": {
#         "* * * * *": [
#             "hotel_management.task.send_reminder_email"
#         ]
#     }
# }

# */5 * * * *: Every 5 minutes.
# 0 0 * * *: Every day at midnight.
# 0 12 * * 1: Every Monday at 12 PM.
# 0 9 * * *: Every day at 9 AM.
# * * * * *: This cron expression means "run the job every minute."

	# "daily": [
	# 	"hotel_management.tasks.daily"
	# ],
	# "hourly": [
	# 	"hotel_management.tasks.hourly"
	# ],
	# "weekly": [
	# 	"hotel_management.tasks.weekly"
	# ],
	# "monthly": [
	# 	"hotel_management.tasks.monthly"
	# ],
# }

# Testing
# -------

# before_tests = "hotel_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hotel_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "hotel_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["hotel_management.utils.before_request"]
# after_request = ["hotel_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["hotel_management.utils.before_job"]
# after_job = ["hotel_management.utils.after_job"]

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
# 	"hotel_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

