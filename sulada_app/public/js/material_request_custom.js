frappe.ui.form.on('Material Request', {
    refresh: function(frm) {
        frm.add_custom_button(__('导出文件'), function() {
            if (!frm.is_new()) {
                frappe.prompt([
                    {
                        fieldname: 'file_type',
                        label: '文件类型',
                        fieldtype: 'Select',
                        options: [
                            {value: 'excel', label: 'Excel (.csv)'},
                            {value: 'csv', label: 'CSV (.csv)'}
                        ],
                        default: 'excel'
                    }
                ],
                function(values) {
                    frappe.call({
                        method: 'sulada_app.export.export_document',
                        args: {
                            doctype: 'Material Request',
                            docname: frm.doc.name,
                            file_type: values.file_type
                        },
                        callback: function(r) {
                            if (r.exc) {
                                frappe.msgprint('导出失败: ' + r.exc);
                            } else if (r.message) {
                                var a = document.createElement('a');
                                a.href = r.message.file_url;
                                a.download = r.message.filename;
                                a.style.display = 'none';
                                document.body.appendChild(a);
                                a.click();
                                document.body.removeChild(a);
                                frappe.msgprint('文件导出成功');
                            }
                        }
                    });
                },
                '选择导出文件类型',
                '导出'
                );
            } else {
                frappe.msgprint('请先保存单据后再导出。');
            }
        });
    }
});
