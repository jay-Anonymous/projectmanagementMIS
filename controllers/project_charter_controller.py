# project_charter_controller.py

import frappe
from taskmanager.doctype.project_charter import ProjectCharter

def create_project_charter(data):
    project_charter = ProjectCharter(data)
    project_charter.insert()
    return project_charter
