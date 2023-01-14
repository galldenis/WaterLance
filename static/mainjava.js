
var button = document.getElementById("get-location-button");
button.addEventListener("click", function() {
    navigator.geolocation.getCurrentPosition(function(position) {
        var lat = position.coords.latitude;
        var lng = position.coords.longitude;
        console.log("Latitude: " + lat + ", Longitude: " + lng);
        var center = {lat , lng}
        console.log(center)
        

    });
});
