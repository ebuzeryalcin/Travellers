// Used onscroll function from this link https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_onscroll
function scrollcard() {
  document.getElementById("scrolling-card");
}

$("#place_description").keyup(function(){
      $("#desc-char").text("Characters left: " + (250 - $(this).val().length));
    });