$(document).ready(function(){
    var path = window.location.pathname;
    segments = trimChar(path, "/").split("/");
    id = segments[segments.length-1];
    $.getJSON("/api/" + id + "/", function(data) {
        if(data.hasOwnProperty("meta")
            && data["meta"]["success"]){
                $('.secret').text(data["data"]["secret"]);
        } else {
            $('.secret').text("Something went wrong");
        }
    });
});

// Trims a specific character, taken from https://stackoverflow.com/a/26156806 //
function trimChar(string, charToRemove) {
    while(string.charAt(0)==charToRemove) {
        string = string.substring(1);
    }

    while(string.charAt(string.length-1)==charToRemove) {
        string = string.substring(0,string.length-1);
    }

    return string;
}