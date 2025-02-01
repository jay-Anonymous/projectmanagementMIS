import frappe
from frappe.model.document import Document

class ProjectCharter(Document):
    def validate(self):
        # Logic for validating the project charter
        if not self.project_name:
            frappe.throw("Project Name is required.")
        if not self.objectives:
            frappe.throw("Objectives are required.")
        if not self.scope:
            frappe.throw("Scope is required.")
        if not self.participants:
            frappe.throw("Participants are required.")
