function temperatura() {
    const num1 = Number(document.getElementById("num1").value);

    if (num1<=0) {
        document.getElementById("resultado").textContent = "Muito Frio!"
    } else if (num1>0 && num1<=15) {
        document.getElementById("resultado").textContent = "Frio!"
    } else if (num1>15 && num1<=25) {
        document.getElementById("resultado").textContent = "Agradável!"
    } else {
        document.getElementById("resultado").textContent = "Calor!"
    }
}