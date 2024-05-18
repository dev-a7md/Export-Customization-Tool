# Copyright (c) 2023, Havenir Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.modules.utils import export_customizations

class ExportCustomizationsTool(Document):
	@frappe.whitelist()
	def export_all(self):
		sync_on_migrate = self.sync_on_migrate
		export_custom_permissions = self.export_custom_permissions
		module_to_export = self.module_to_export

		cust_doctypes = frappe.db.sql("""
			select dt
			from `tabCustom Field`
			group by dt
		""",as_dict = True)

		data = []
		sql_data = frappe.db.sql("""
			select parent doctype, creation, modified, role
			from `tabCustom DocPerm`
		""",as_dict = True)
		for record in sql_data:
			doctype = record.get("doctype")
			doctype_permissions = frappe.db.get_list("DocPerm",{"parent": doctype}, pluck = "role")
			if record.get("role") not in doctype_permissions:
				data.append(record)
			else:
				if record.get("creation") != record.get("modified"):
					data.append(record)
		
		doctypes = []
		for row in data:
			if row["doctype"] in doctypes:
				continue
			doctypes.append(row["doctype"])

		for cust_d in cust_doctypes:
			if cust_d.get("dt") not in doctypes:
				doctypes.append(cust_d.get("dt"))

		docs_len = len(doctypes)
		success = 0
		
		for doctype in doctypes:
			try:
				export_customizations(doctype = doctype,module = module_to_export,sync_on_migrate = sync_on_migrate,with_permissions = export_custom_permissions)
				success += 1
			except Exception as e:
				continue
		frappe.msgprint(f"{success} Of {docs_len} Doctypes Exported!")
