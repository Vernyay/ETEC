import 'dart:io';

void main() {
  String? input = stdin.readLineSync();
  if (input == null) return;

  List<String> partes = input.split(' ');
  int a = int.parse(partes[0]);
  int b = int.parse(partes[1]);
  int c = int.parse(partes[2]);
  int d = int.parse(partes[3]);

  if (b > c && d > a && (c + d) > (a + b) && c > 0 && d > 0 && a % 2 == 0) {
    print("Valores aceitos");
  } else {
    print("Valores nao aceitos");
  }
}