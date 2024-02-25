

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





// ESTO ES PARA Q ME HACER COMO UN DOBLECKECK DE QUE QUIERO BORRAR EL ARCHIVO
document.addEventListener('DOMContentLoaded', function () {
    // Obtén todos los formularios con la clase "borrarForm"
    const borrarForms = document.querySelectorAll('.borrarForm');

    // Agrega un evento de clic a cada formulario
    borrarForms.forEach(function (form) {
        form.addEventListener('submit', function (event) {
            // Pregunta al usuario si está seguro de borrar
            const confirmacion = confirm('¿Estás seguro de que quieres eliminar este archivo?');

            // Si el usuario cancela, previene el envío del formulario
            if (!confirmacion) {
                event.preventDefault();
            }
        });
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


document.getElementById("toglesidebar").addEventListener("click", ocultarMenu);