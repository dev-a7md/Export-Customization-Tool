import frappe
from datetime import datetime


def create_custom_field_log(doc,method):
    log_doc = frappe.new_doc("Doctypes Customs Log")
    log_doc.field_name = doc.fieldname
    log_doc.is_custom_field = 1
    log_doc.creator = frappe.session.user
    log_doc.doctype_name = doc.dt
    log_doc.reference = doc.name
    log_doc.created_at = datetime.now()
    log_doc.insert()

def create_custom_perm_log(doc,method):
    log_doc = frappe.new_doc("Doctypes Customs Log")
    log_doc.role = doc.role
    log_doc.is_custom_perm = 1
    log_doc.creator = frappe.session.user
    log_doc.doctype_name = doc.parent
    log_doc.reference = doc.name
    log_doc.created_at = datetime.now()
    log_doc.insert()
