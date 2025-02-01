# billing_controller.py

import frappe
from taskmanager.doctype.billing import Billing

def create_billing(data):
    billing = Billing(data)
    billing.insert()
    return billing
