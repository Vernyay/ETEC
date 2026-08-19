function checar() {
    const num1 = Number(document.getElementById("num1").value);

    if (num1<=80) {
        document.getElementById("resultado").textContent = "Velocidade permitida!";
    } else if (num1<=100 && num1>80) {
        document.getElementById("resultado").textContent = "Multa Leve!";
    } else {
        document.getElementById("resultado").textContent = "Multa Grave!";
    }
}