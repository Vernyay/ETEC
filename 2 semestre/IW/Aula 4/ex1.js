function semana() {
    const num1 = Number(document.getElementById("num1").value);

    if (num1==1) {
        document.getElementById("resultado").textContent = "Domingo!";
    } else if (num1==2) {
        document.getElementById("resultado").textContent = "Segunda!";
    } else if (num1==3) {
        document.getElementById("resultado").textContent = "Terça!";
    } else if (num1==4) {
        document.getElementById("resultado").textContent = "Quarta!";
    } else if (num1==5) {
        document.getElementById("resultado").textContent = "Quinta!";
    } else if (num1==6) {
        document.getElementById("resultado").textContent = "Sexta!";
    } else if (num1==7) {
        document.getElementById("resultado").textContent = "Sábado!";
    } else {
        document.getElementById("resultado").textContent = "Dia inválido!";
    }
}