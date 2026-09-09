<?php
require_once 'login.php';

$mensagem = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $login = new Login();
    $login->setUsuario($_POST['usuario'] ?? '');
    $login->setSenha($_POST['senha'] ?? '');

    if ($login->validar($login->getUsuario)) {
        $mensagem = "<p style='color: green;'>Login efetuado com sucesso!</p>";
    } else {
        $mensagem = "<p style='color: red;'>Usuário ou senha incorretos!</p>";
    }
}