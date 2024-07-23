from frappe import _

def get_data():
    return [
        {
            "label": _("Purchase Order Dashboard"),
            "icon": "octicon octicon-file-directory",
            "items": [
                {
                    "type": "page",
                    "name": "purchase-order-dashboard",
                    "label": _("Purchase Order Dashboard"),
                    "description": _("Dashboard for viewing and exporting Purchase Orders."),
                    "onboard": 1,
                },
            ]
        }
    ]

