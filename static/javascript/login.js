const form = document.getElementById('form');
const email = document.getElementById('email');
const password = document.getElementById('password');

form.addEventListener('submit', e => {
    e.preventDefault();
    if (validateInputs()) {
        form.submit() 
    }
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');
    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
}

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
}

const validateInputs = () => {
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    var em = false
    var pass = false

    if(emailValue === '') {
        setError(email, 'Se requiere su email');
    } else if (!isValidEmail(emailValue)) {
        setError(email, 'Ingrese una direccion de correo valida');
    } else if (emailValue.length > 30 ) {
        setError(email, "Maximo de caracteres alcanzado")
    } else {
        setSuccess(email);
        em = true
    }

    if (passwordValue === '') {
        setError(password, 'Contraseña requerida');
    } else if (passwordValue.length < 8) {
        setError(password, 'La contraseña debe tener al menos 8 caracteres');
    } else if (passwordValue.length > 16) {
        setError(password, 'La contraseña no debe tener más de 16 caracteres');
    } else {
        setSuccess(password);
        pass = true;
    }
    
    if( em && pass){
        return true
    }else{
        return false
    }

};
