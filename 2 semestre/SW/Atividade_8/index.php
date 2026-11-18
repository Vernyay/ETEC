<?php
chdir(__DIR__ . '/model');
ob_start();

require_once __DIR__ . '/controller/UsuarioController.php';
require_once __DIR__ . '/controller/ImovelController.php';

$acao = isset($_GET['acao']) ? $_GET['acao'] : 'listarImovel';
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Imobiliária</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div class="container">
            <a class="marca" href="index.php">Imobiliária</a>
            <nav>
                <a href="index.php?acao=listarImovel">Imóveis</a>
                <a href="index.php?acao=cadImovel">Novo Imóvel</a>
                <a href="index.php?acao=listarUsuario">Usuários</a>
                <a href="index.php?acao=cadUsuario">Novo Usuário</a>
            </nav>
        </div>
    </header>
    <div class="container">
        <?php
        switch ($acao) {
            case 'cadUsuario':
                include __DIR__ . '/view/cadUsuario.php';
                break;

            case 'listarUsuario':
            case 'listUsuario':
                include __DIR__ . '/view/listUsuario.php';
                break;

            case 'cadImovel':
                include __DIR__ . '/view/cadImovel.php';
                break;

            case 'editarImovel':
                $imovel = ImovelController::editar(isset($_GET['id']) ? $_GET['id'] : 0);
                include __DIR__ . '/view/cadImovel.php';
                break;

            case 'excluirImovel':
                ImovelController::excluir(isset($_GET['id']) ? $_GET['id'] : 0);
                include __DIR__ . '/view/listImovel.php';
                break;

            case 'listarImovel':
            default:
                include __DIR__ . '/view/listImovel.php';
                break;
        }
        ?>
    </div>
<?php ob_end_flush(); ?>
</body>
</html>
