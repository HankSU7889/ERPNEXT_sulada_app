app_name = "sulada_app"
app_title = "Sulada App"
app_publisher = "SuHongKai"
app_description = "sulada Internal Use"
app_email = "923918316@qq.com"
app_license = "mit"

# 添加翻译路径
translated_languages = ["zh"]

#设置定时任务自动生成出入库单据
scheduler_events = {
    "cron": {
        "0 23 * * *": [
            "sulada_app.tasks.in_and_out_data_task"
        ]
    }
}


#自动获取当天出入库数据
doc_events = {
    "In and out data": {
        "before_insert": "sulada_app.events.in_and_out_data.before_insert"
    }
}

# 在 sulada_app/hooks.py 覆盖物料需求时间

scheduler_events = {
    "cron": {
        "0 23 * * *": [
            "erpnext.stock.reorder_item.reorder_item"
        ]
    }
}

# 注册补丁
patches = [
    "sulada_app.patches.update_reorder_item_cron"
]

# 采购订单页面保存后增加筛选包含SULADA条码

doc_events = {
    "Purchase Order": {
        "before_save": "sulada_app.events.purchase_order.before_save"
    },
    "Delivery Note": {
        "before_save": "sulada_app.events.purchase_order.before_save"
    }
}

# sulada_app/hooks.py采购订单和物料需求页面增加导出按钮

doctype_js = {
    "Purchase Order": "public/js/purchase_order_custom.js",
    "Material Request": "public/js/material_request_custom.js",
    "Delivery Note": "public/js/delivery_note_custom.js"
}

# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sulada_app/css/sulada_app.css"
# app_include_js = "/assets/sulada_app/js/sulada_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/sulada_app/css/sulada_app.css"
# web_include_js = "/assets/sulada_app/js/sulada_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sulada_app/public/scss/website"

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
# app_include_icons = "sulada_app/public/icons.svg"

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
# 	"methods": "sulada_app.utils.jinja_methods",
# 	"filters": "sulada_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sulada_app.install.before_install"
# after_install = "sulada_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sulada_app.uninstall.before_uninstall"
# after_uninstall = "sulada_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sulada_app.utils.before_app_install"
# after_app_install = "sulada_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sulada_app.utils.before_app_uninstall"
# after_app_uninstall = "sulada_app.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sulada_app.notifications.get_notification_config"

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
# 		"sulada_app.tasks.all"
# 	],
# 	"daily": [
# 		"sulada_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"sulada_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sulada_app.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sulada_app.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sulada_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sulada_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sulada_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sulada_app.utils.before_request"]
# after_request = ["sulada_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["sulada_app.utils.before_job"]
# after_job = ["sulada_app.utils.after_job"]

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
# 	"sulada_app.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

