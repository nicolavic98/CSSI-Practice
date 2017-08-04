function alerting() {
  alert("my alert");
}
function hidePs() {
  $("p").hide();
}

  alerting();

  $(document).ready(HidePs);


  ---------

  //html
  Enter your text here: <input type="text">
    <br>
    You typed: <span id="result"></span>
  //js
  function moveText() {
    var input_text = $('input').val();
    $("#result").text(input_text);
  }
  $('#result').text(user_text);
