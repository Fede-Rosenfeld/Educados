
// ESTO ES LA MISMA VALIDACION QUE EL REGISTER PERO PARA EDITAR USUARIO
const form = document.getElementById('form');
const name = document.getElementById('nombre');
const lastname = document.getElementById('lastname');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form.addEventListener('submit', e => {
    e.preventDefault(); // Previene el envío automático del formulario
    if (validateInputs()) {
        form.submit(); // Envía el formulario si la validación es exitosa
    }
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success');
};

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
};

const validateInputs = () => {
    const nameValue = name.value.trim();
    const lastnameValue = lastname.value.trim();
    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const password2Value = password2.value.trim();
    var na = false;
    var lna = false;
    var user = false;
    var em = false;
    var pass = false;
    var pass2 = false;

    if (nameValue === '') {
        setError(name, 'Nombre requerido');
    } else if (nameValue.length > 15) {
        setError(name, 'Máximo de caracteres alcanzado');
    } else {
        setSuccess(name);
        na = true;
    }

    if (lastnameValue === '') {
        setError(lastname, 'Apellido requerido');
    } else if (lastnameValue.length > 15) {
        setError(lastname, 'Máximo de caracteres alcanzado');
    } else {
        setSuccess(lastname);
        lna = true;
    }

    if (usernameValue === '') {
        setError(username, 'Nombre de usuario requerido');
    } else if (usernameValue.length > 12) {
        setError(username, 'Máximo de caracteres alcanzado');
    } else {
        setSuccess(username);
        user = true;
    }

    if (emailValue === '') {
        setError(email, 'Se requiere su email');
    } else if (!isValidEmail(emailValue)) {
        setError(email, 'Ingrese una dirección de correo válida');
    } else if (emailValue.length > 30) {
        setError(email, 'Máximo de caracteres alcanzado');
    } else {
        setSuccess(email);
        em = true;
    }

    if (passwordValue === '') {
        setError(password, 'Contraseña requerida');
    } else if (passwordValue.length < 8 || passwordValue.length > 16) {
        setError(password, 'La contraseña debe tener entre 8 y 16 caracteres');
    } else {
        setSuccess(password);
        pass = true;
    }

    if (password2Value === '') {
        setError(password2, 'Por favor, confirme su contraseña');
    } else if (password2Value !== passwordValue) {
        setError(password2, 'Las contraseñas no coinciden');
    } else {
        setSuccess(password2);
        pass2 = true;
    }

    if (na && lna && user && em && pass && pass2) {
        return true;
    } else {
        return false;
    }
};



function ocultarMenu() {
    let menu = document.getElementById("menu");
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
  }
}
document.getElementById("toglesidebar").addEventListener("click", ocultarMenu);


// Obtener referencia al modal y al botón de cerrar
const modal = document.getElementById('modal');
const cerrarModal = document.getElementById('cerrarModal');

// Obtener referencia al botón que abre el modal
const abrirModalBtn = document.getElementById('abrirModalBtn');

// Función para abrir el modal
const abrirModal = () => {
    modal.style.display = 'block';
};

// Función para cerrar el modal
const cerrarModalFunc = () => {
    modal.style.display = 'none';
};

// Evento de clic en el botón que abre el modal
abrirModalBtn.addEventListener('click', abrirModal);

// Evento de clic en el botón de cerrar el modal
cerrarModal.addEventListener('click', cerrarModalFunc);

// Evento para cerrar el modal si se hace clic fuera de él
window.addEventListener('click', (event) => {
    if (event.target === modal) {
        cerrarModalFunc();
    }
});

// Evento para cerrar el modal si se presiona la tecla Esc
document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
        cerrarModalFunc();
    }
});



// ESTO ES PARA QUE SE VEA BORROSO LA CONTRASENA
const passwordCell = document.getElementById('filaContraseña');
const passwordBlur = document.getElementById('passwordBlur');

passwordCell.addEventListener('click', () => {
    passwordBlur.classList.toggle('active');
});