document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('register-form');
    const loginForm = document.getElementById('login-form');
    const recoverForm = document.getElementById('recover-form');

    const showMessage = (message, isSuccess) => {
        const messageContainer = document.createElement('div');
        messageContainer.textContent = message;
        messageContainer.className = isSuccess ? 'success-message' : 'error-message';
        document.body.appendChild(messageContainer);
        setTimeout(() => {
            messageContainer.remove();
        }, 5000);
    };

    if (registerForm) {
        registerForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(registerForm);
            const response = await fetch(registerForm.action, {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            if (result.success) {
                showMessage(result.message, true);
                registerForm.reset();
            } else {
                showMessage(result.message, false);
            }
        });
    }

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(loginForm);
            const response = await fetch(loginForm.action, {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            if (result.success) {
                showMessage(result.message, true);
                window.location.href = result.redirect;
            } else {
                showMessage(result.message, false);
            }
        });
    }

    if (recoverForm) {
        recoverForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(recoverForm);
            const response = await fetch(recoverForm.action, {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            if (result.success) {
                showMessage(result.message, true);
                recoverForm.reset();
            } else {
                showMessage(result.message, false);
            }
        });
    }

    const signInButton = document.getElementById('sign-in');
    const signUpButton = document.getElementById('sign-up');
    const recoverButton = document.getElementById('recover');
    const signInRecoverButton = document.getElementById('sign-in-recover');

    if (signInButton) {
        signInButton.addEventListener('click', () => {
            document.querySelector('.container.register').classList.add('hide');
            document.querySelector('.container.login').classList.remove('hide');
        });
    }

    if (signUpButton) {
        signUpButton.addEventListener('click', () => {
            document.querySelector('.container.login').classList.add('hide');
            document.querySelector('.container.register').classList.remove('hide');
        });
    }

    if (recoverButton) {
        recoverButton.addEventListener('click', () => {
            document.querySelector('.container.login').classList.add('hide');
            document.querySelector('.container.recov').classList.remove('hide');
        });
    }

    if (signInRecoverButton) {
        signInRecoverButton.addEventListener('click', () => {
            document.querySelector('.container.recov').classList.add('hide');
            document.querySelector('.container.login').classList.remove('hide');
        });
    }
});
