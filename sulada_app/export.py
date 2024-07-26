import frappe
from frappe.utils.response import build_response
import csv
import io
from frappe.utils.file_manager import save_file

@frappe.whitelist()
def export_document(doctype, docname, file_type='excel'):
    doc = frappe.get_doc(doctype, docname)
    
    # 权限检查
    if doc.docstatus == 0 and doc.get("__islocal"):
        frappe.throw("请先保存单据后再导出。")
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    # 根据单据类型选择合适的表头和数据
    if doctype == "Purchase Order":
        headers = ['物料编码', '物料名称', '数量', '条码']
        items = doc.items
        supplier_name = doc.supplier  # 获取供应商名称
    elif doctype == "Material Request":
        headers = ['物料编码', '物料名称', '数量', '仓库']
        items = doc.items
        supplier_name = "No_Supplier"  # Material Request 可能没有供应商字段
    else:
        frappe.throw(f"不支持的单据类型: {doctype}")
    
    # 写入表头
    writer.writerow(headers)
    
    # 写入数据
    for item in items:
        item_doc = frappe.get_doc("Item", item.item_code)
        custom_barcode = item_doc.get('custom_barcode', '')
        
        if doctype == "Purchase Order":
            row = [
                item.item_code,
                item.item_name,
                item.qty,
                item.custom_barcode
            ]
        elif doctype == "Material Request":
            row = [
                item.item_code,
                item.item_name,
                item.qty,
                item.warehouse
            ]
        
        writer.writerow(row)


    
    content = output.getvalue().encode('utf-8-sig')
    
    filename = f"{supplier_name}_{doc.name}.csv"

    # 保存文件并获取文件 URL
    file_url = save_file(
        filename,
        content,
        doctype,
        doc.name,
        folder=None,
        is_private=1,
        df=None
    ).file_url

    return {
        'file_url': file_url,
        'filename': filename
    }
