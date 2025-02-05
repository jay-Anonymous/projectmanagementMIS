import frappe

def create_project(data):
    """Create a new project."""
    project = frappe.get_doc({
        'doctype': 'Project',
        'project_name': data.get('project_name'),
        'start_date': data.get('start_date'),
        'end_date': data.get('end_date'),
        'budget': data.get('budget'),
        'milestones': data.get('milestones'),
        'project_manager': data.get('project_manager')
    })
    project.insert()
    return project

def update_task(task_id, data):
    """Update an existing task."""
    task = frappe.get_doc('Task', task_id)
    task.update(data)
    task.save()

def log_expense(expense_data):
    """Log a new expense."""
    expense = frappe.get_doc({
        'doctype': 'Expense',
        'amount': expense_data.get('amount'),
        'description': expense_data.get('description'),
        'project': expense_data.get('project')
    })
    expense.insert()
    return expense

def create_task(data):
    """Create a new task."""
    task = frappe.get_doc({
        'doctype': 'Task',
        'task_name': data.get('task_name'),
        'project': data.get('project'),
        'assigned_to': data.get('assigned_to'),
        'due_date': data.get('due_date'),
        'priority': data.get('priority'),
        'status': 'Open'
    })
    task.insert()
    return task

def update_project(project_id, data):
    """Update an existing project."""
    project = frappe.get_doc('Project', project_id)
    project.update(data)
    project.save()

def track_progress(task_id, progress):
    """Track progress of a task."""
    task = frappe.get_doc('Task', task_id)
    task.progress = progress
    task.save()

def budget_tracking(project_id, budget_data):
    """Track budget for a project."""
    project = frappe.get_doc('Project', project_id)
    project.budget = budget_data.get('budget')
    project.save()
