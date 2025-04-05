function updateStrengthMeter() {
    const password = document.getElementById('password').value;
    const strengthBar = document.querySelector('.progress-bar');
    const strengthText = document.getElementById('strength-text');

    let strength = 0;

    if (password.length > 5) strength += 1;
    if (password.length > 8) strength += 1;
    if (/[A-Z]/.test(password)) strength += 1;
    if (/[0-9]/.test(password)) strength += 1;
    if (/[\W]/.test(password)) strength += 1;

    switch (strength) {
        case 0:
            strengthBar.style.width = '0%';
            strengthText.textContent = '';
            strengthBar.className = 'progress-bar';
            break;
        case 1:
            strengthBar.style.width = '20%';
            strengthText.textContent = 'Very Weak';
            strengthBar.className = 'progress-bar bg-danger';
            break;
        case 2:
            strengthBar.style.width = '40%';
            strengthText.textContent = 'Weak';
            strengthBar.className = 'progress-bar bg-warning';
            break;
        case 3:
            strengthBar.style.width = '60%';
            strengthText.textContent = 'Medium';
            strengthBar.className = 'progress-bar bg-info';
            break;
        case 4:
            strengthBar.style.width = '80%';
            strengthText.textContent = 'Strong';
            strengthBar.className = 'progress-bar bg-success';
            break;
        case 5:
            strengthBar.style.width = '100%';
            strengthText.textContent = 'Very Strong';
            strengthBar.className = 'progress-bar bg-success';
            break;
    }
}
