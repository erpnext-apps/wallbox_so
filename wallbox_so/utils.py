import frappe
from erpnext.selling.doctype.sales_order.sales_order import make_delivery_note

def update_delivery_from_so(doc, method):
	if method == "on_update_after_submit":
		if doc.meta.get_field("workflow_state") and doc.workflow_state == "Installation Completed":
			dn = make_delivery_note(doc.name)
			dn.save()
			dn.submit()
	elif method == "on_cancel":
		dn_name = frappe.get_value("Delivery Note Item", {"against_sales_order": doc.name}, "parent")
		if dn_name:
			dn = frappe.get_doc("Delivery Note", dn_name)
			dn.cancel()
