// Copyright (c) 2023, Havenir Solutions and contributors
// For license information, please see license.txt

frappe.ui.form.on('Export Customizations Tool', {
	refresh: function(frm) {
		
	},
	export: function(frm) {
		if (frm.doc.doctypes.length > 0 && frm.doc.doctypes != [] && frm.doc.module_to_export){
			frm.doc.doctypes.forEach(record => {
				frappe.call({
					method: "frappe.modules.utils.export_customizations",
					args: {
						doctype: record.doctype_name,
						module: frm.doc.module_to_export,
						sync_on_migrate: frm.doc.sync_on_migrate,
						with_permissions: frm.doc.export_custom_permissions
					}
				});
			});
		}else{
			frappe.msgprint("Please Specify Doctypes And Module To Export!")
		}
	},
	export_all: function(frm){
		if ( frm.doc.module_to_export){
			frappe.confirm('Are you sure you want to proceed?',
			() => {
				frm.call("export_all").then(r=>{})
			}, () => {
			})
		}else{
			frappe.msgprint("Please Specify Module To Export!")
		}
	}
});
