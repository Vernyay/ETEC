function calcular() {
  
  const num1 = Number(document.getElementById("num1").value);
  const num2 = Number(document.getElementById("num2").value);
  
 
  const operacao = document.getElementById("operacao").value;
  
  let resultado = 0;

  switch (operacao) {
    case "somar":
      resultado = num1 + num2;
      break;
    case "subtrair":
      resultado = num1 - num2;
      break;
    case "multiplicar":
      resultado = num1 * num2;
      break;
    case "dividir":
    
      if (num2 === 0) {
        document.getElementById("resultado").textContent = "Erro: Divisão por zero!";
        return;
      }
      resultado = num1 / num2;
      break;
    default:
      document.getElementById("resultado").textContent = "Operação inválida.";
      return;
  }

  document.getElementById("resultado").textContent = "Resultado: " + resultado;
}