// Cuando la página se carga completamente
window.onload = function() {
    // Seleccionar el formulario de inicio de sesión y el formulario de registro
    var loginForm = document.querySelector('form[action="/login"]');
    var registerForm = document.querySelector('form[action="/register"]');

    // Si el formulario de inicio de sesión existe
    if (loginForm) {
        // Cuando se envía el formulario de inicio de sesión
        loginForm.onsubmit = function(e) {
            // Seleccionar los campos de correo electrónico y contraseña
            var email = document.querySelector('input[name="email"]');
            var password = document.querySelector('input[name="password"]');
            
            // Si el campo de correo electrónico está vacío
            if (!email.value) {
                // Mostrar una alerta y prevenir el envío del formulario
                alert('Por favor, ingrese su correo electrónico.');
                e.preventDefault();
            } 
            // Si el campo de contraseña está vacío
            else if (!password.value) {
                // Mostrar una alerta y prevenir el envío del formulario
                alert('Por favor, ingrese su contraseña.');
                e.preventDefault();
            }
        }
    }

    // Si el formulario de registro existe
    if (registerForm) {
        // Cuando se envía el formulario de registro
        registerForm.onsubmit = function(e) {
            // Seleccionar los campos de nombre, correo electrónico y contraseña
            var name = document.querySelector('input[name="name"]');
            var email = document.querySelector('input[name="email"]');
            var password = document.querySelector('input[name="password"]');
            
            // Si el campo de nombre está vacío
            if (!name.value) {
                // Mostrar una alerta y prevenir el envío del formulario
                alert('Por favor, ingrese su nombre completo.');
                e.preventDefault();
            } 
            // Si el campo de correo electrónico está vacío
            else if (!email.value) {
                // Mostrar una alerta y prevenir el envío del formulario
                alert('Por favor, ingrese su correo electrónico.');
                e.preventDefault();
            } 
            // Si el campo de contraseña está vacío
            else if (!password.value) {
                // Mostrar una alerta y prevenir el envío del formulario
                alert('Por favor, ingrese su contraseña.');
                e.preventDefault();
            }
        }
    }
}

// Cuando el documento está listo
$(document).ready(function(){
    // Cuando se hace clic en el botón "Agregar", mostrar/ocultar el formulario de agregar
    $("#addButton").click(function(){
        $("#addForm").toggle();
    });
    // Cuando se hace clic en el botón "Editar", mostrar/ocultar el formulario de editar
    $("#editButton").click(function(){
        $("#editForm").toggle();
    });
    // Cuando se hace clic en el botón "Eliminar", mostrar/ocultar el formulario de eliminar
    $("#deleteButton").click(function(){
        $("#deleteForm").toggle();
    });

    // Cuando se hace clic en el icono del menú, mostrar/ocultar el menú
    $('.menu-icon').click(function() {
        $('.menu').toggle();
    });
});