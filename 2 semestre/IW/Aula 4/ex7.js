function cargo() {
    const cargo = String(document.getElementById("num1").value);

    if (cargo=="gerente") {
        document.getElementById("resultado").textContent = "Salário: R$ 5.000!";
    } else if (cargo=="programador") {
        document.getElementById("resultado").textContent = "Salário: R$ 4.000!";
    } else if (cargo=="estagiário") {
        document.getElementById("resultado").textContent = "Salário: R$ 1.500!";
    } else {
        document.getElementById("resultado").textContent = "Cargo não identificado!";
    }
}