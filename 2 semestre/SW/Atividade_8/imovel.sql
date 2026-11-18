CREATE DATABASE IF NOT EXISTS imobiliaria;

USE imobiliaria;

CREATE TABLE imovel (
    id INT(4) NOT NULL AUTO_INCREMENT,
    descricao VARCHAR(200) NOT NULL,
    foto VARCHAR(30),
    valor DECIMAL(9,2) NOT NULL,
    tipo CHAR(1) NOT NULL,
    PRIMARY KEY (id)
);
