function comparar() {
    const num1 = Number(document.getElementById("num1").value);
    const num2 = Number(document.getElementById("num2").value);

    if (num1>num2) {
        document.getElementById("resultado").textContent = num1 + " é maior que " + num2 + " !";
    } else if (num1<num2) {
        document.getElementById("resultado").textContent = num1 + " é menor que " + num2 + " !";
    } else {
        document.getElementById("resultado").textContent = "Ambos são iguais!"
    }
}