function alerting() {
  alert("You know we're right ;)");
}


function stuffToDoOnLoad() {
  setTimeout(alerting, 2000);
}

$(document).ready(stuffToDoOnLoad);
