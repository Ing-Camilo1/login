document.addEventListener('DOMContentLoaded', () => {
    const logoutBtn = document.getElementById('logout-btn');

    if (logoutBtn) {
        logoutBtn.addEventListener('click', () => {
            fetch('/logout', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'  // Asegura que la solicitud sea tratada como AJAX
                },
                body: JSON.stringify({})  // Enviar cuerpo vacío ya que el endpoint no espera datos
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/';  // Redirige a la página de login
                } else {
                    alert('Error al cerrar sesión');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al cerrar sesión');
            });
        });
    }
});
