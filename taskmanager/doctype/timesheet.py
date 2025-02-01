import frappe
from frappe.model.document import Document

class Timesheet(Document):
    def validate(self):
        # Logic for validating the timesheet
        if self.hours_worked <= 0:
            frappe.throw("Hours worked must be greater than zero.")
        if not self.employee_name:
            frappe.throw("Employee name is required.")
        if not self.project:
            frappe.throw("Project is required.")
        if not self.date:
            frappe.throw("Date is required.")
