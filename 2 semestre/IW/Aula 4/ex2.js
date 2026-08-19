function salario() {
    const num1 = Number(document.getElementById("num1").value);

    if (num1>=500) {
        var salary = num1 - (num1*0.10);
        document.getElementById("resultado").textContent = "Seu salario é :R$" + num1 + " e foi descontado R$" + salary + " !";
    } else if (num1>=200 && num1<500) {
        var salary = num1 - (num1*0.05)
        document.getElementById("resultado").textContent = "Seu salario é :R$" + num1 + " e foi descontado R$" + salary + " !";
    } else {
        document.getElementById("resultado").textContent = "Sem Desconto!";
    }
}