$(function () {
    $("input[required]").parent().prev().append($("<span>").text("*").addClass("required"));
})
$(document).ready(function () {

    var now = new Date();

    var day = ("0" + now.getDate()).slice(-2);
    var month = ("0" + (now.getMonth() + 1)).slice(-2);

    var hours = now.getHours();
    var minutes = now.getMinutes();
    var today = now.getFullYear() + "-" + (month) + "-" + (day) + "T" + (hours) + ":" + (minutes);
    $("#date").val(today);
});