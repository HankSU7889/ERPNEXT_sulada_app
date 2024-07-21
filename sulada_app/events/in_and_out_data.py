import frappe

def before_insert(doc, method):
    frappe.logger().info("Before Insert for In and out data triggered")
    
    # 获取今天的日期
    todays_date = frappe.utils.today()

    # 计算采购入库数量
    purchase_total_qty = frappe.db.sql("""
        SELECT SUM(item.qty) as total_qty FROM `tabPurchase Receipt Item` item
        JOIN `tabPurchase Receipt` pr ON item.parent = pr.name
        WHERE pr.docstatus = 1 AND pr.posting_date = %s
    """, todays_date, as_dict=1)

    # 计算销售出库数量
    sales_total_qty = frappe.db.sql("""
        SELECT SUM(item.qty) as total_qty FROM `tabDelivery Note Item` item
        JOIN `tabDelivery Note` dn ON item.parent = dn.name
        WHERE dn.docstatus = 1 AND dn.posting_date = %s
    """, todays_date, as_dict=1)

    # 检查并更新采购入库数量
    if purchase_total_qty and purchase_total_qty[0].get('total_qty') is not None:
        doc.todays_material_total = purchase_total_qty[0].get('total_qty')
    else:
        doc.todays_material_total = 0

    # 检查并更新销售出库数量
    if sales_total_qty and sales_total_qty[0].get('total_qty') is not None:
        doc.todays_sales_total = sales_total_qty[0].get('total_qty')
    else:
        doc.todays_sales_total = 0

    frappe.logger().info("In and out data document updated with totals")

