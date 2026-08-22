<?php
class Produto {
    private string $nome;
    private float $preco_uni;
    private int $quant;
    private float $perc;

    public function setNome($nome){
        $this->nome = $nome;
    }
    public function setPreco_Uni($preco_uni){
        $this->preco_uni = $preco_uni;
    }
    public function setQuant($quant){
        $this->quant = $quant;
    }
    public function setPerc($perc){
        $this->perc = $perc;
    }
    public function getNome(){
        return $this->nome;
    }
    public function getPreco_Uni(){
        return $this->preco_uni;
    }
    public function getQuant(){
        return $this->quant;
    }
    public function getPerc(){
        return $this->perc;
    }
    public function calcularValorTotal(){
        return $this->preco_uni*$this->quant;
    }
    public function desconto(){
        $valorTotal = $this->calcularValorTotal();
        $valorDesconto = $valorTotal * ($this->perc/100);
        return $valorTotal - $valorDesconto;
    }
    public function estaEmEstoqueBaixo() {
        if ($this->quant<5){
            return True;
        }
    }
    
}