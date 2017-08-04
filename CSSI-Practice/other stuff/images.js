


function togglefight2() {
  $("#fight2").toggle();
}
function togglefight3() {
  $("#fight3").toggle();
}

function stuffToDoOnLoad() {
  $("#proof1").click(togglefight2);
  $("#proof2").click(togglefight3);
}
$(document).ready(stuffToDoOnLoad);
