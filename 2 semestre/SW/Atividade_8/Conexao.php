<?php
class Conexao{

    private $servername = "localhost:3306";
    private $username = "root";
    private $password = "123456";
    private $database = "imobiliaria";
    private $conecion;

    public function getConection(){
        if (is_null($this->conecion)) {
            $this->conecion = new PDO('mysql:host='.$this->servername.';dbname='.$this->database, $this->username, $this->password);
            $this->conecion->setAttribute(\PDO::ATTR_ERRMODE, \PDO::ERRMODE_EXCEPTION);
            $this->conecion->exec('set names utf8');
        }
        return $this->conecion;
    }
}