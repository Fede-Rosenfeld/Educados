

$(document).ready(function () {
  $('.footer-links').click(function () {
      $('body, html').animate({
          scrollTop: '0px'
      }, 300);
  });

  $(window).scroll(function () {
      if ($(this).scrollTop() > 0) {
          $('.footer-links').addClass('mostrar');
      } else {
          $('.footer-links').removeClass('mostrar');
      }
  });
});

function myFunction() {
    var x = document.getElementById("myNavbar");
    if (x.className === "navbar") {
      x.className += " responsive";
    } else {
      x.className = "navbar";
    }
  }