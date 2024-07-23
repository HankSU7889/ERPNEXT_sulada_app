import frappe
from frappe.utils import getdate
import openpyxl
from openpyxl.utils import get_column_letter
from io import BytesIO
from frappe.utils.file_manager import save_file

@frappe.whitelist()
def get_purchase_orders():
    purchase_orders = frappe.get_all("Purchase Order", fields=["name", "supplier"], order_by="creation desc", limit=10)
    return purchase_orders

@frappe.whitelist()
def export_purchase_order_to_excel(purchase_order):
    # 创建一个新的工作簿和工作表
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Purchase Order Details"

    # 设置表头
    headers = ["Item Code", "Item Name", "Quantity", "Rate", "Amount"]
    ws.append(headers)

    # 获取采购订单明细
    po_doc = frappe.get_doc("Purchase Order", purchase_order)
    for item in po_doc.items:
        row = [
            item.item_code,
            item.item_name,
            item.qty,
            item.rate,
            item.amount
        ]
        ws.append(row)

    # 自动调整列宽
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter  # 获取列字母
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column].width = adjusted_width

    # 保存为临时文件
    file_name = f"Purchase_Order_{purchase_order}.xlsx"
    with BytesIO() as f:
        wb.save(f)
        f.seek(0)
        file_doc = save_file(file_name, f, "Purchase Order", purchase_order, is_private=0)
    
    return file_doc.file_url

