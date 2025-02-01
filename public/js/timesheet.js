// JavaScript for Timesheet Filling Form
document.getElementById('timesheet-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const employeeName = document.getElementById('employee-name').value;
    const project = document.getElementById('project').value;
    const hoursWorked = document.getElementById('hours-worked').value;
    const date = document.getElementById('date').value;

    // Here you would typically send the data to the server
    console.log('Timesheet submitted:', {
        employeeName,
        project,
        hoursWorked,
        date
    });

    alert('Timesheet submitted successfully!');
});
