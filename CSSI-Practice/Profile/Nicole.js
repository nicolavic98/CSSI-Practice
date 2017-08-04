//function disappear() {
//  $("#Paris-photo").toggleClass("hidden");
//}
 //$(document).ready(function() {
//     $("#Hide-button").click(disappear);
//   }
//)
//alert("Welcome to Nikoala's World!");

function alerting() {
  alert("Welcome to Nikoala's World!");
}
function toggleParis() {
  $("#Paris-photo").toggle();
}
function moveText() {
  var input_text = $('input').val();
  $("#result").text(input_text);
  alert(input_text);
}

function stuffToDoOnLoad() {
  setTimeout(alerting, 2000);
  $("#Hide-button").click(toggleParis);
  $("#Show").click(moveText);
}

$(document).ready(stuffToDoOnLoad);
