"use strict";


function fetchTemperatureAndHumidity() {
    $.ajax({
        type: "get",
        url: "/temperature_and_humidity",
        data: "",
        dataType: "json",
        success: function (data) {
            const temperature = data.temperature
            const humidity = data.humidity
            document.getElementById("temperature").innerHTML = temperature
            document.getElementById("humidity").innerHTML = humidity
        }
    })
}


window.onload = function() {
    setInterval("fetchTemperatureAndHumidity()", 5000);
}
