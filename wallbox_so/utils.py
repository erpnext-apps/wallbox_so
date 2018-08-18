import frappe
from frappe.model.mapper import get_mapped_doc

def consume_stock_by_so(doc, method):
	se = get_mapped_doc("Sales Order", doc.name, {
		"Sales Order": {
			"doctype": "Stock Entry",
			"field_map": {
				"delivery_date": "posting_date"
			}
		},
		"Sales Order Item" : {
			"doctype": "Stock Entry Detail",
			"field_map": {
				"warehouse": "s_warehouse"
			}
		}
	}, ignore_permissions=1)
	se.purpose = "Material Issue"
	se.docstatus = 1
	se.insert(ignore_permissions=1)
	if doc.meta.get_field("wb_stock_entry"):
		doc.wb_stock_entry = se.name

def mark_so_completed(doc, method):
	doc.update_status("Closed")
	doc.save()

def cancel_stock_entry(doc, method):
	if doc.meta.get_field("wb_stock_entry") and doc.wb_stock_entry:
		se = frappe.get_doc("Stock Entry", doc.wb_stock_entry)
		se.cancel()
		doc.db_set("wb_stock_entry", "")

@frappe.whitelist()
def get_installers(doctype, txt, searchfield, start, page_len, filters):
	txt = "%{}%".format(txt)
	return frappe.db.sql("""select ur.name, concat_ws(' ', ur.first_name, ur.middle_name, ur.last_name)
		from `tabUser` ur join `tabHas Role` hr
		where hr.role="Installer" and ur.name=hr.parent and ur.enabled=1
			and ur.docstatus < 2
			and ur.name not in ("Guest", "Administrator")
			and (concat_ws(' ', ur.first_name, ur.middle_name, ur.last_name) like %(txt)s)
		order by
			case when ur.name like %(txt)s then 0 else 1 end,
			case when concat_ws(' ', ur.first_name, ur.middle_name, ur.last_name) like %(txt)s
				then 0 else 1 end,
			ur.name asc
		limit %(start)s, %(page_len)s""", dict(start=start, page_len=page_len, txt=txt))
