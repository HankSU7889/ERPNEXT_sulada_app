import frappe

def before_save(doc, method):
    for item in doc.items:
        if item.item_code:
            try:
                barcodes = frappe.get_all("Item Barcode", filters={'parent': item.item_code}, fields=["barcode"], limit=1)
                if barcodes:
                    item.custom_barcode = barcodes[0].barcode
                else:
                    item.custom_barcode = ''
            except frappe.PermissionError:
                frappe.msgprint(f"您没有足够的权限来访问物料 {item.item_code} 的条码信息。请联系您的经理，以获得访问权。")

