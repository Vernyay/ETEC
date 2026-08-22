<?php

require_once 'Produto.php';

if ($_SERVER['REQUEST_METHOD']==='POST') {
    $produto = new Produto();

    $produto->setNome($_POST['nome']);
    $produto->setPreco_Uni($_POST['precouni']);
    $produto->setQuant($_POST['quant']);
    $produto->setPerc($_POST['perc']);

    $nome = $produto->getNome();
    $total = $produto->calcularValorTotal();
    $desc = $produto->desconto();
    $estoque = $produto->estaEmEstoqueBaixo();
    include "resultado.php";
}