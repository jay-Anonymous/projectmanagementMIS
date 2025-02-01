// JavaScript for Milestone Signoff Form
document.getElementById('milestone-signoff-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const milestoneName = document.getElementById('milestone-name').value;
    const clientName = document.getElementById('client-name').value;
    const signature = document.getElementById('signature').value;

    // Here you would typically send the data to the server
    console.log('Milestone Signoff submitted:', {
        milestoneName,
        clientName,
        signature
    });

    alert('Milestone Signoff submitted successfully!');
});
