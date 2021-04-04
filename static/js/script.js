// Used onscroll function from this link https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_onscroll
function scrollcard() {
  document.getElementById("scrolling-card");
}
// Used function from this link https://stackoverflow.com/questions/36719982/error-message-when-a-user-enters-more-characters-than-max-length-on-text-area
$("#place_description").keyup(function(){
      $("#desc-char").text("Characters left: " + (250 - $(this).val().length));
    });