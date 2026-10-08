import 'dart:io';
import 'cadastro.dart';

void main() {
  print("-" * 35);
  print(" BEM-VINDO AO CADASTRO DE ALUNOS ");
  print("-" * 35);

  List<Aluno> alunos = [];
  int totalAlunos = 3;

  for (int i = 0; i < totalAlunos; i++) {
    print("\n--- Cadastro do ${i + 1}º Aluno ---");
    
    stdout.write("Digite o nome do aluno: ");
    String nome = stdin.readLineSync() ?? "";

    stdout.write("Digite o RA do aluno: ");
    String ra = stdin.readLineSync() ?? "";

    Set<String> linguagens = {};
    print("Digite as linguagens que conhece (digite 'sair' para encerrar esta lista):");
    while (true) {
      stdout.write("Linguagem: ");
      String lang = stdin.readLineSync()?.trim() ?? "";
      if (lang.toLowerCase() == 'sair' || lang.isEmpty) break;
      linguagens.add(lang);
    }

    Map<String, List<double>> notas = {};
    print("\nCadastro de disciplinas (cada uma precisa de 4 notas).");
    print("Digite 'sair' no nome da disciplina para finalizar as notas.");
    
    while (true) {
      stdout.write("Nome da disciplina (ou 'sair'): ");
      String disciplina = stdin.readLineSync()?.trim() ?? "";
      if (disciplina.toLowerCase() == 'sair' || disciplina.isEmpty) break;

      List<double> atividades = [];
      print("Digite as 4 notas:");
      
      for (int j = 0; j < 4; j++) {
        stdout.write("  Nota da atividade ${j + 1}: ");
        double nota = double.tryParse(stdin.readLineSync() ?? "") ?? 0.0;
        atividades.add(nota);
      }
      
      notas[disciplina] = atividades;
    }

    alunos.add(Aluno(nome: nome, ra: ra, linguagens: linguagens, notas: notas));
  }

  print("\n" + "=" * 45);
  print("       RELATÓRIO FINAL DOS ALUNOS       ");
  print("=" * 45);

  for (var aluno in alunos) {
    print("\nAluno: ${aluno.nome}");
    print("RA: ${aluno.ra}");
    print("Linguagens conhecidas: ${aluno.linguagens.join(', ')}");
    print("Desempenho por Disciplina:");

    if (aluno.notas.isEmpty) {
      print("  Nenhuma disciplina cadastrada.");
    } else {
      aluno.notas.forEach((disciplina, listaNotas) {
        double media = aluno.calcularMedia(disciplina);
        print("  -> $disciplina");
        print("     Notas: $listaNotas");
        print("     Média Ponderada: ${media.toStringAsFixed(2)}");
      });
    }
    print("-" * 45);
  }
}