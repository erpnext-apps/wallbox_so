import frappe
from erpnext.selling.doctype.sales_order.sales_order import make_delivery_note

def update_delivery_from_so(doc, method):
	if doc.meta.get_field("workflow_state") and doc.workflow_state == "Installation Completed":
		dn = make_delivery_note(doc.name)
		dn.save()
		dn.submit()
