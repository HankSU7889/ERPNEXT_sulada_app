def In_and_out_data_task():
    frappe.logger().info("Daily task executed at 23:00")
    # 创建一个空的 "In and out data" 单据
    doc = frappe.new_doc("In and out data")
    # 保存单据
    doc.save()
    frappe.logger().info("In and out data document created and saved")
