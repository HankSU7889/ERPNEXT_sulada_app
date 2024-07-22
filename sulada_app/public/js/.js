frappe.ui.form.on('Purchase Order', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__('Export to Excel'), function() {
                frappe.call({
                    method: "sulada_app.utils.export_purchase_order_to_excel",
                    args: {
                        purchase_order: frm.doc.name
                    },
                    callback: function(r) {
                        if (r.message) {
                            window.open(r.message);
                        }
                    }
                });
            });
        }
    }
});

