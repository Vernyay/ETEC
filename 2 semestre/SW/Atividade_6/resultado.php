<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Resultado do Aluno</title>
</head>
<body>
    <?php if (isset($nome)): ?>
        <p>Nome: <?= $nome ?></p>
        <p>Média: <?= number_format($media, 2) ?></p>
        <p>Presença: <?= number_format($presenca, 2) ?>%</p>
        <p>Situação: <?= $resultado ?></p>
    <?php else: ?>
        <p>Nenhum dado enviado. Preencha o formulário primeiro.</p>
    <?php endif; ?>
</body>
</html>