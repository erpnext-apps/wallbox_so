# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "wallbox_so"
app_title = "Wallbox SO"
app_publisher = "Frappe Technologies"
app_description = "App to create Delivery Note in SO Workflow"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@erpnext.com"
app_license = "MIT"


doc_events = {
	"Sales Order": {
		"before_submit" : "wallbox_so.utils.consume_stock_by_so",
		"on_submit": "wallbox_so.utils.mark_so_completed",
		"on_cancel" : "wallbox_so.utils.cancel_stock_entry"
	}
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/wallbox_so/css/wallbox_so.css"
# app_include_js = "/assets/wallbox_so/js/wallbox_so.js"

# include js, css files in header of web template
# web_include_css = "/assets/wallbox_so/css/wallbox_so.css"
# web_include_js = "/assets/wallbox_so/js/wallbox_so.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "wallbox_so.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "wallbox_so.install.before_install"
# after_install = "wallbox_so.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "wallbox_so.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"wallbox_so.tasks.all"
# 	],
# 	"daily": [
# 		"wallbox_so.tasks.daily"
# 	],
# 	"hourly": [
# 		"wallbox_so.tasks.hourly"
# 	],
# 	"weekly": [
# 		"wallbox_so.tasks.weekly"
# 	]
# 	"monthly": [
# 		"wallbox_so.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "wallbox_so.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "wallbox_so.event.get_events"
# }
