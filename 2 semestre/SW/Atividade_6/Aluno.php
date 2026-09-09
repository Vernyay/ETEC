<?php
class Aluno {
    private string $nome;
    private float $nota1;
    private float $nota2;
    private float $nota3;
    private int $faltas;

    public function setNome($nome) {
        $this->nome = $nome;
    }
    public function setNota1($nota1) {
        $this->nota1 = $nota1;
    }
    public function setNota2($nota2) {
        $this->nota2 = $nota2;
    }
    public function setNota3($nota3) {
        $this->nota3 = $nota3;
    }
    public function setFaltas($faltas) {
        $this->faltas = $faltas;
    }

    public function getNome() {
        return $this->nome;
    }
    public function getNota1() {
        return $this->nota1;
    }
    public function getNota2() {
        return $this->nota2;
    }
    public function getNota3() {
        return $this->nota3;
    }
    public function getFaltas() {
        return $this->faltas;
    }

    public function calcularMedia() {
        return ($this->nota1 + $this->nota2 + $this->nota3) / 3;
    }

    public function calcularPresenca() {
        $totalAulas = 80;
        $presencas = $totalAulas - $this->faltas;
        return ($presencas / $totalAulas) * 100;
    }

    public function mostrarResultado() {
        $media = $this->calcularMedia();
        $presenca = $this->calcularPresenca();

        if ($presenca < 75) {
            return "Reprovado por Falta";
        } elseif ($media < 5) {
            return "Reprovado";
        } elseif ($media >= 5 && $media <= 7) {
            return "Recuperação";
        } else {
            return "Aprovado";
        }
    }
}