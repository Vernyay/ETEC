<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Tela de Login</title>
</head>
<body>
    <h2>Login</h2>
    
    <?php 
    if (isset($mensagem)) {
        echo $mensagem;
    }
    ?>

    <form action="controller.php" method="POST">
        <div>
            <label>Usuário:</label>
            <input type="text" name="usuario" required>
        </div>
        <div>
            <label>Senha:</label>
            <input type="password" name="senha" required>
        </div>
        <button type="submit">Entrar</button>
    </form>
</body>
</html>