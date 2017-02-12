
function AJAXCall(messageSource) {
    var xmlhttp = new XMLHttpRequest();
    // var message = document.getElementById(messageSource).value;
    message = encodeURIComponent(message);
    var params = "request=addQuestion&message=" + message;

    document.getElementById(messageSource).value = "";

    xmlhttp.open("POST", "/cgi-bin/questionController.py", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send(params);

    getResults()
}