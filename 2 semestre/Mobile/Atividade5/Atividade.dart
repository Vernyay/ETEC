import 'dart:io';

class Livro {
  
  String titulo;
  String autor;
  int anoPublicacao;

  Livro(this.titulo, this.autor, this.anoPublicacao);

  void exibirInformacoes() {
    print('----------------------------------------');
    print('Título: $titulo');
    print('Autor: $autor');
    print('Ano de Publicação: $anoPublicacao');
    print('----------------------------------------');
  }
}

void main() {
  Livro livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954);
  Livro livro2 = Livro('Dom Casmurro', 'Machado de Assis', 1899);

  print('=== Relatório de Livros Cadastrados ===\n');

  livro1.exibirInformacoes();
  livro2.exibirInformacoes();
}