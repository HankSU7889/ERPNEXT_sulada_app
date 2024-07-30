import frappe

def before_save(doc, method):
    for item in doc.items:
        if item.item_code:
            # 查找符合条件的条码
            barcodes = frappe.get_all("Item Barcode", filters={'parent': item.item_code}, fields=["barcode"])
            if barcodes:
                # 筛选出符合条件的条码
                sulada_barcodes = [barcode['barcode'] for barcode in barcodes if barcode['barcode'].endswith('SULADA')]
                if sulada_barcodes:
                    # 选择第一个符合条件的条码
                    item.custom_barcode = sulada_barcodes[0]
                else:
                    item.custom_barcode = ''
            else:
                item.custom_barcode = ''

