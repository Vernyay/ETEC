<?php

class login {
    private $usuario;
    private $senha;
    
    public function setUsuario($usuario){
        $this->usuario = $usuario;
    }
    
    public function getUsuario(){
        return $this->usuario;
    }
    
    public function setSenha($senha){
        $this->senha = $senha;
    }
    
    public function getSenha(){
        return  $this->senha;
    }
    
    public function validar($senhaHash){
        $usuarioCadastrado = "admin";
            $senhaHashCadastrada = 'e10adc3949ba59abbe56e057f20f883e';
    
            if ($this->usuario === $usuarioCadastrado && password_verify($this->senha, $senhaHashCadastrada)) {
                return true;
            }
            
            return false;
    }
}
