import frappe
from frappe.model.document import Document

class MilestoneSignoff(Document):
    def validate(self):
        # Logic for validating the milestone signoff
        if not self.milestone_name:
            frappe.throw("Milestone Name is required.")
        if not self.client_name:
            frappe.throw("Client Name is required.")
        if not self.signature:
            frappe.throw("Signature is required.")
