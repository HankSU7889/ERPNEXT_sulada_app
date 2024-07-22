# 在 sulada_app/patches/update_reorder_item_cron.py 文件中

import frappe

def execute():
    # 获取所有调度任务
    scheduler_jobs = frappe.get_all("Scheduled Job Type", filters={"method": "erpnext.stock.reorder_item.reorder_item"})

    # 更新 cron 表达式
    for job in scheduler_jobs:
        doc = frappe.get_doc("Scheduled Job Type", job.name)
        doc.cron_format = "0 23 * * *"
        doc.save()

