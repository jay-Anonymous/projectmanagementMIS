# timesheet_controller.py

import frappe
from taskmanager.doctype.timesheet import Timesheet

def create_timesheet(data):
    timesheet = Timesheet(data)
    timesheet.insert()
    return timesheet
