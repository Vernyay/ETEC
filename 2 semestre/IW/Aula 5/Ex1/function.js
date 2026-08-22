function calcular(operacao) {
    let input1 = prompt("Digite o primeiro número:");
    let input2 = prompt("Digite o segundo número:");

    let num1 = parseFloat(input1);
    let num2 = parseFloat(input2);

    if (isNaN(num1) || isNaN(num2)) {
        alert("Por favor, digite números válidos!");
        return;
    }

    let res = 0;

    switch (operacao) {
        case '+':
            res = num1 + num2;
            break;
        case '-':
            res = num1 - num2;
            break;
        case '*':
            res = num1 * num2;
            break;
        case '/':
            if (num2 === 0) {
                alert("Erro! Divisão por zero não é permitida.");
                return;
            }
            res = num1 / num2;
            break;
        }

            
    document.getElementById("resultado").innerText = "Resultado: " + res;
    }