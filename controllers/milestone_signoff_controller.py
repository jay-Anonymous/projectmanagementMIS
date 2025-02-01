# milestone_signoff_controller.py

import frappe
from taskmanager.doctype.milestone_signoff import MilestoneSignoff

def create_milestone_signoff(data):
    milestone_signoff = MilestoneSignoff(data)
    milestone_signoff.insert()
    return milestone_signoff
