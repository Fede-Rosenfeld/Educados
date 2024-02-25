
function ocultarMenu() {
    let menu = document.getElementById("menu");
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
  }
}



document.getElementById("toglesidebar").addEventListener("click", ocultarMenu);