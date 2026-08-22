var img1 = "HTML5_logo_and_wordmark.svg.webp";
var img2 = "1_rM8t0CGxBDN6eaJGgJyJwA.jpg";
var img3 = "OIP.webp";
var img4 = "Python-Symbol.png";
var img5 = "R.jpg";


function Trocar(){
    document.getElementById("figura").src = img1;
    let aux = img1;
    img1 = img2;
    img2 = img3;
    img3 = img4;
    img4 = img5;
    img5 = aux;
    }