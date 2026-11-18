<?php
$imovel = isset($imovel) ? $imovel : null;

$descricao = ($imovel) ? $imovel->getDescricao() : '';
$foto      = ($imovel) ? $imovel->getFoto() : '';
$valor     = ($imovel) ? $imovel->getValor() : '';
$tipo      = ($imovel) ? $imovel->getTipo() : '';
$id        = ($imovel) ? $imovel->getId() : '';
?>
<h1><?php echo ($imovel) ? 'Editar Imóvel' : 'Cadastro de Imóvel'; ?></h1>
<hr>
<form name="cadImovel" id="cadImovel" action="" method="post">
    Descrição: <input type="text" name="descricao" id="descricao" maxlength="200" value="<?php echo $descricao; ?>"><br/>
    Foto (nome do arquivo): <input type="text" name="foto" id="foto" maxlength="30" value="<?php echo $foto; ?>"><br/>
    Valor: <input type="number" name="valor" id="valor" min="0" step="0.01" value="<?php echo $valor; ?>"><br/>
    Tipo:
    <select name="tipo" id="tipo">
        <option value="">Selecione</option>
        <option value="C" <?php echo ($tipo == 'C') ? 'selected' : ''; ?>>Casa</option>
        <option value="A" <?php echo ($tipo == 'A') ? 'selected' : ''; ?>>Apartamento</option>
        <option value="T" <?php echo ($tipo == 'T') ? 'selected' : ''; ?>>Terreno</option>
    </select><br/><br/>
    <input type="hidden" name="id" id="id" value="<?php echo $id; ?>">
    <input type="submit" name="btnSalvar" id="btnSalvar" value="Salvar">
</form>
<?php
if(isset($_POST['btnSalvar'])){

    require_once '../controller/ImovelController.php';
    call_user_func(array('ImovelController','salvar'));

    header('Location: index.php?acao=listarImovel');
    exit;
}
?>
