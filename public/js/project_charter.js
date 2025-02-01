// JavaScript for Project Charter Form
document.getElementById('project-charter-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const projectName = document.getElementById('project-name').value;
    const objectives = document.getElementById('objectives').value;
    const scope = document.getElementById('scope').value;
    const participants = document.getElementById('participants').value;

    // Here you would typically send the data to the server
    console.log('Project Charter submitted:', {
        projectName,
        objectives,
        scope,
        participants
    });

    alert('Project Charter submitted successfully!');
});
