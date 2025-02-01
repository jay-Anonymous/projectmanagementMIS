import frappe
from frappe.model.document import Document

class ResourceAllocation(Document):
    def validate(self):
        # Logic for validating resource allocation
        if not self.project:
            frappe.throw("Project is required.")
        if not self.resources:
            frappe.throw("Resources are required.")
        if not self.allocation_date:
            frappe.throw("Allocation Date is required.")
