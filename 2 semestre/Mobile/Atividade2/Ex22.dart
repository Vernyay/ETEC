import 'dart:io';

void main() {
  String? input = stdin.readLineSync();
  if (input == null) return;
  
  double valorTotal = double.parse(input);
  int centavos = (valorTotal * 100).round();

  List<int> notas = [10000, 5000, 2000, 1000, 500, 200];
  List<int> moedas = [100, 50, 25, 10, 5, 1];

  print("NOTAS:");
  for (int nota in notas) {
    int quantidade = centavos ~/ nota;
    centavos %= nota;
    double valorReais = nota / 100;
    print("$quantidade nota(s) de R\$ ${valorReais.toStringAsFixed(2)}");
  }

  print("MOEDAS:");
  for (int moeda in moedas) {
    int quantidade = centavos ~/ moeda;
    centavos %= moeda;
    double valorReais = moeda / 100;
    print("$quantidade moeda(s) de R\$ ${valorReais.toStringAsFixed(2)}");
  }
}