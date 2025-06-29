function handleLogin() {
    var rollNumber = document.getElementById('rollNumber').value;
    var password = document.getElementById('password').value;
    var message = document.getElementById('message');

    // Remove hardcoded credentials and implement AJAX call
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rollNumber: rollNumber, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Login successful!");
            window.location.href = "dashboard.html";
        } else {
            message.textContent = "Invalid roll number or password.";
        }
    })
    .catch(error => {
        console.error('Error:', error);
        message.textContent = "An error occurred. Please try again.";
    });
}

function handleYellowBoxClick() {
    alert("There will be updates before exams!");
}
