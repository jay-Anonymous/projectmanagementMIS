import frappe
from frappe.model.document import Document

class Billing(Document):
    def validate(self):
        # Logic for validating billing
        if not self.project:
            frappe.throw("Project is required.")
        if not self.billing_type:
            frappe.throw("Billing Type is required.")
        if self.amount <= 0:
            frappe.throw("Amount must be greater than zero.")
        if not self.billing_date:
            frappe.throw("Billing Date is required.")
