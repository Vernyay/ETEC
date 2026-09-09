<?php
require_once 'Aluno.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $aluno = new Aluno();

    $aluno->setNome($_POST['nome']);
    $aluno->setNota1($_POST['nota1']);
    $aluno->setNota2($_POST['nota2']);
    $aluno->setNota3($_POST['nota3']);
    $aluno->setFaltas($_POST['faltas']);

    $nome = $aluno->getNome();
    $media = $aluno->calcularMedia();
    $presenca = $aluno->calcularPresenca();
    $resultado = $aluno->mostrarResultado();

    include "resultado.php";
}