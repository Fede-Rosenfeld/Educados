// ACA VAN TODAS LAS VALIDACIONES       
// ESTO LO TENGO Q ARREEGLARRRRR

function validacioncomentario() {
    var textarea = document.getElementById('com');
    var contenido = textarea.value;
    if (contenido === '' || contenido.length < 20) {
        textarea.classList.add("error");
        textarea.placeholder = 'El comentario debe tener al menos 20 caracteres.';
        textarea.value = "";
        return false; // Evita que se envíe el formulario si hay un error.
    } else {
        alert('El comentario se ha mandado exitosamente.');
        textarea.classList.add("correct");
        textarea.placeholder = "";
        textarea.value = "";
        return true; // Permite que el formulario se envíe si la validación es exitosa.
    }
}

// ACA TERMINAN TODAS LAS VALIDACIONES


// ESTE ES EL MODAL PARA ESCRIBIR COMENTARIOS
// Obtener referencias a los elementos del DOM
const iconosComentarios1 = document.querySelectorAll(".comment");
const modalesComentarios1 = document.querySelectorAll(".modal");
const cerrarModales1 = document.querySelectorAll(".close");

// Abrir el modal al hacer clic en el icono de comentarios
iconosComentarios1.forEach((icono, index) => {
    icono.addEventListener("click", () => {
        modalesComentarios1[index].style.display = "block";
    });
});

// Cerrar el modal al hacer clic en la "X" o fuera de él
cerrarModales1.forEach((btn, index) => {
    btn.addEventListener("click", () => {
        modalesComentarios1[index].style.display = "none";
    });
});

// Cerrar el modal al hacer clic fuera de él
window.addEventListener("click", (event) => {
    modalesComentarios1.forEach((modal) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});

// ESTE ES EL MODAL PARA VER COMENTARIOS

// Obtener referencias a los elementos del DOM
const iconosComentarios = document.querySelectorAll(".comentarios");
const modalesComentarios = document.querySelectorAll(".modal-coms");
const cerrarModales = document.querySelectorAll(".close-modal");

// Abrir el modal al hacer clic en el icono de comentarios
iconosComentarios.forEach((icono, index) => {
    icono.addEventListener("click", () => {
        modalesComentarios[index].style.display = "block";
    });
});

// Cerrar el modal al hacer clic en la "X" o fuera de él
cerrarModales.forEach((btn, index) => {
    btn.addEventListener("click", () => {
        modalesComentarios[index].style.display = "none";
    });
});

// Cerrar el modal al hacer clic fuera de él
window.addEventListener("click", (event) => {
    modalesComentarios.forEach((modal) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});



// ESTE ES EL FILTRO DE BUSQUEDA
document.addEventListener('DOMContentLoaded', function () {
    var formFiltro = document.getElementById('form_filtro');
    var nombreBuscar = document.getElementById('nombrebuscar');
    var cajas = document.querySelectorAll('.caja');
    var mensajeNoCoincidencias = document.getElementById('mensaje_no_coincidencias');
  
    formFiltro.addEventListener('submit', function (event) {
        event.preventDefault();
  
        var valorBusqueda = nombreBuscar.value.trim().toLowerCase();
        var resultadosEncontrados = false;
  
        cajas.forEach(function (caja) {
            var nombreCaja = caja.querySelector('.nomarch h3').textContent.toLowerCase();
  
            if (nombreCaja.includes(valorBusqueda)) {
                caja.style.display = 'block';
                resultadosEncontrados = true;
            } else {
                caja.style.display = 'none';
            }
        });
  
        if (resultadosEncontrados) {
            mensajeNoCoincidencias.style.display = 'none';
        } else {
            mensajeNoCoincidencias.style.display = 'block';
        }
    });
  });
  




function ocultarMenu() {
    let menu = document.getElementById("menu");
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
  }
}
document.getElementById("toglesidebar").addEventListener("click", ocultarMenu);

// Event Listeners
document.getElementById("buscar").addEventListener("click", filtrarCajas);

document.getElementById("form_filtro").addEventListener("submit", function (event) {
    event.preventDefault(); // Evita la recarga de la página al enviar el formulario
    filtrarCajas();
});

