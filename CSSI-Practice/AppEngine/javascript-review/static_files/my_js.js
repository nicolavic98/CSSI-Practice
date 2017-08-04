function stuffToDoWhenFaded() {
  alert("Done fading out");
}

function stuffToDoOnLoad() {
  $("#hello").fadeOut(1500, stuffToDoWhenFaded);
  $("emoji").click(function() {
    $("#emoji").fadeOut(1000);
  })
}

$(document).ready(stuffToDoOnLoad);
