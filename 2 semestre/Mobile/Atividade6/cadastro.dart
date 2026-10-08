import 'dart:io';

class Aluno {
    String nome;
    String ra;
    Set<String> linguagens;
    Map<String, List<double>> notas;
    
    Aluno({
    required this.nome,
    required this.ra,
    required this.linguagens,
    required this.notas,
  });
  double calcularMedia(String disciplina) {
    List<double>? n = notas[disciplina];
    if (n == null || n.length < 4) return 0.0;

    double somaPesos = 4 + 4 + 6 + 6;
    double somaNotas = (n[0] * 4) + (n[1] * 4) + (n[2] * 6) + (n[3] * 6);

    return somaNotas / somaPesos;
  }
}