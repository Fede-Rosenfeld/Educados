// MATERIAS //

// Obtiene el botón y el modal
var button = document.querySelector(".show-list-button");
var modal = document.getElementById("modal");

// Obtiene el botón para cerrar el modal
var closeButton = document.getElementById("close");

// Obtiene el campo de búsqueda
var searchInput = document.getElementById("search");

// Agrega un evento de clic al botón para mostrar el modal
button.addEventListener("click", function() {
    modal.style.display = "block";
});

// Agrega un evento de clic al botón de cierre para ocultar el modal
closeButton.addEventListener("click", function() {
    modal.style.display = "none";
});

// Cierra el modal si el usuario hace clic fuera de él
window.addEventListener("click", function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
});


// TIPOS DE ARCHIVO //

// Obtiene el botón y el modal para Tipos de Archivo
var fileTypeButton = document.querySelector("#showFileTypeListButton");
var fileTypeModal = document.getElementById("fileTypeModal");

// Obtiene el botón para cerrar el modal de Tipos de Archivo
var closeFileTypeButton = document.getElementById("closeFileTypeModal");

// Agrega un evento de clic al botón para mostrar el modal de Tipos de Archivo
fileTypeButton.addEventListener("click", function() {
    fileTypeModal.style.display = "block";
});

// Agrega un evento de clic al botón de cierre para ocultar el modal de Tipos de Archivo
closeFileTypeButton.addEventListener("click", function() {
    fileTypeModal.style.display = "none";
});

// Cierra el modal de Tipos de Archivo si el usuario hace clic fuera de él
window.addEventListener("click", function(event) {
    if (event.target == fileTypeModal) {
        fileTypeModal.style.display = "none";
    }
});



// #################### PARA BORRAR LOS TIPOS O MATERIAS ###############//
// Es funcion onclick 
function eliminarMateria(materiaId) {
    if (confirm('¿Estás seguro de que deseas eliminar esta materia?')) {
        document.getElementById('deleteForm' + materiaId).submit();
    }
}

function eliminarTipo(tipoId) {
    if (confirm('¿Estás seguro de que deseas eliminar esta materia?')) {
        document.getElementById('deleteForm' + tipoId).submit();
    }
}

// #################### END FEDE ###########//