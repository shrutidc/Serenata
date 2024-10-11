document.getElementById('nameForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    // Store the name in localStorage
    localStorage.setItem('userName', name);
    // Redirect to the welcome page
    window.location.href = 'welcome.html';
});