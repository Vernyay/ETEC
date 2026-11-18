<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tela da Calculadora</title>
</head>
<body>
    <form action="index.php" method="post">
        <label for="valor1">Primeiro Numero</label>
        <input type="number" name="valor1" id="valor1" required>
        <label for="operacao">Operação</label>
        <select name="operacao" id="operacao" required>
            <option value="0">---Selecione---</option>
            <option value="1">Soma</option>
            <option value="2">Subtração</option>
            <option value="3">Multiplicação</option>
            <option value="4">Divisão</option>
            <option value="5">Exponenciação</option>
        </select>
        <label for="valor2">Segundo Numero</label>
        <input type="number" name="valor2" id="valor2" required>
        <button type="submit" name="btnCalcule" id="btnCalcule">Calcular</button>
    </form>
</body>
</html>