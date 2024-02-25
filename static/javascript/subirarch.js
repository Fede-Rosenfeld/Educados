


function inicializarInput() {
    let input = document.getElementById("inputTag");
    let imageName = document.getElementById("imageName");
    input.addEventListener("change", () => {
      let inputImage = input.files[0];  //esto lo que hace es poner el nombre del archivo que selecciona el usuario
      imageName.innerText = inputImage.name;
    });
  }

function validarFormulario() {
    var nombreArchivo = document.getElementById('nomarch').value;
    var tipoArchivo = document.getElementById('tipo').value;
    var materiaArchivo = document.getElementById('materias').value;
    var archivo = document.getElementById('inputTag').files[0];

    if (nombreArchivo.trim() === '' || tipoArchivo === 'Tipos' || materiaArchivo === 'Materia' || !archivo) {
        alert('Por favor, complete todos los campos y cargue un archivo.');
        contenedor-subirarch.classList.add('campo-error')
        return false;
    }
    else if(archivo && !archivo.name.toLowerCase().endsWith('.pdf')){
        alert('EL ARCHIVO TIENE QUE SER PDF!!');
    }
    else {
        alert('Se ha publicado correctamente tu archivo.');
        window.location.reload();
        return true;
    }
}

function ocultarMenu() {
  let menu = document.getElementById("menu");
  if (menu.style.display === "block") {
      menu.style.display = "none";
  } else {
      menu.style.display = "block";
}
}



//LISTA DE EVENTOS

document.getElementById("form").addEventListener("submit",  e => {
  e.preventDefault(); // Evita la recarga de la página al enviar el formulario
  if(validarFormulario()){
    form.submit()
  }
});
document.getElementById("toglesidebar").addEventListener("click", ocultarMenu);

// Llama a la función para inicializar el input
  inicializarInput();


