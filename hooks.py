app_name = "taskmanager"
app_title = "Taskmanager"
app_publisher = "gathee"
app_description = "Project manager tool"
app_email = "gerald@upande.com"
app_license = "gpl-3.0"

# Include JS and CSS files in header of desk.html
app_include_css = "/assets/taskmanager/css/styles.css"
app_include_js = "/assets/taskmanager/js/timesheet.js"
app_include_js = "/assets/taskmanager/js/project_charter.js"
app_include_js = "/assets/taskmanager/js/milestone_signoff.js"
app_include_js = "/assets/taskmanager/js/reports.js"

# Document Events
doc_events = {
    "Timesheet": {
        "on_submit": "taskmanager.api.timesheet.on_submit",
        "on_cancel": "taskmanager.api.timesheet.on_cancel"
    },
    "Project": {
        "on_update": "taskmanager.api.project.on_update"
    }
}

# Permissions
permission_query_conditions = {
    "Timesheet": "taskmanager.api.permission.get_permission_query_conditions",
}

has_permission = {
    "Timesheet": "taskmanager.api.permission.has_permission",
}
