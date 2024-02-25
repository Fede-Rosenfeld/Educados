


function ocultarMenu() {
    let menu = document.getElementById("menu");
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
  }
}
document.getElementById("toglesidebar").addEventListener("click", ocultarMenu);


document.addEventListener('DOMContentLoaded', function () {
  var favoriteForms = document.querySelectorAll('.favoritos-form');

  favoriteForms.forEach(function (form) {
    form.addEventListener('submit', function (event) {
      // Prevenir el envío automático del formulario
      event.preventDefault();

      // Mostrar una ventana de confirmación
      var confirmar = confirm('¿Estás seguro de que quieres quitar de favoritos?');

      // Si el usuario hace clic en "Aceptar" en la ventana de confirmación, envía el formulario
      if (confirmar) {
        form.submit();
      } else {
        alert('Operación cancelada');
      }
    });
  });
});


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
