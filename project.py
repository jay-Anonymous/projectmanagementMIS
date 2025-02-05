import frappe
from frappe.model.document import Document
from frappe import ValidationError

class Project(Document):
    def validate(self):
        if not self.project_name:
            raise ValidationError("Project name is required.")
        if not self.start_date or not self.end_date:
            raise ValidationError("Start and end dates are required.")
        if self.start_date > self.end_date:
            raise ValidationError("Start date cannot be after end date.")

class Task(Document):
    def validate(self):
        if not self.task_name:
            raise ValidationError("Task name is required.")
        if not self.project:
            raise ValidationError("Project is required.")
        if not self.assigned_to:
            raise ValidationError("Assigned to is required.")
        if not self.due_date:
            raise ValidationError("Due date is required.")

class Milestone(Document):
    def validate(self):
        if not self.milestone_name:
            raise ValidationError("Milestone name is required.")
        if not self.project:
            raise ValidationError("Project is required.")

class Resource(Document):
    def validate(self):
        if not self.resource_name:
            raise ValidationError("Resource name is required.")
        if not self.task:
            raise ValidationError("Task is required.")

class Expense(Document):
    def validate(self):
        if not self.amount:
            raise ValidationError("Amount is required.")
        if not self.description:
            raise ValidationError("Description is required.")
        if not self.project:
            raise ValidationError("Project is required.")
