# Copyright (c) 2023, DV and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = get_columns()
	data = []
	sql_data = frappe.db.sql("""
		select parent doctype, creation, modified, role
		from `tabCustom DocPerm`
	""", as_dict = 1)

	for record in sql_data:
		doctype = record.get("doctype")
		doctype_permissions = frappe.db.get_list("DocPerm",{"parent": doctype}, pluck = "role")
		if record.get("role") not in doctype_permissions:
			data.append(record)
		else:
			if record.get("creation") != record.get("modified"):
				data.append(record)
	
	full_data = []
	doctypes = []
	for row in data:
		count = 0
		if row["doctype"] in doctypes:
			continue
		for record in data:
			if row["doctype"] == record["doctype"]:
				count += 1

		doctypes.append(row["doctype"])
		full_data.append({
			"doctype": row["doctype"],
			"custom_permissions": count
		})
	return columns, full_data


def get_columns():
	cols = [
		{
			"label": "Doctype",
			"fieldname": "doctype",
			"fieldtype": "Link",
			"options": "DocType",
			"width": 200
		},
		{
			"label": "Custom Permissions",
			"fieldname": "custom_permissions",
			"fieldtype": "Int",
			"width": 100
		}
	]
	return cols