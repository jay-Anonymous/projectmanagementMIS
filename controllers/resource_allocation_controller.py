# resource_allocation_controller.py

import frappe
from taskmanager.doctype.resource_allocation import ResourceAllocation

def create_resource_allocation(data):
    resource_allocation = ResourceAllocation(data)
    resource_allocation.insert()
    return resource_allocation
