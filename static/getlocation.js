window.addEventListener('load', () => {
    if (!document.cookie.match(/^(.;)?\slatitude\s=\s[^;]+(.)?$/) || !document.cookie.match(/^(.;)?\slongitude\s=\s[^;]+(.)?$/)){
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showLocation);
        }
    }
})

function showLocation(position){
    // document.cookie = 'latitude=' + position.coords.latitude + '; path=/'
    // document.cookie = 'longitude=' + position.coords.longitude + '; path=/'
    // var xmlHttp = new XMLHttpRequest();
    // xmlHttp.open( "GET", "/?latitude=" + position.coords.latitude + "&longitude=" + position.coords.longitude, false ); // false for synchronous request
    // xmlHttp.send( null );
    // return xmlHttp.responseText;
    window.location.href = "/?latitude=" + position.coords.latitude + "&longitude=" + position.coords.longitude;
}