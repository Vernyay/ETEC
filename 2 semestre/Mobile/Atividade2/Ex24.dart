import 'dart:io';
import 'dart:math';

void main() {
  String? input = stdin.readLineSync();
  if (input == null) return;

  List<String> partes = input.split(' ');
  double a = double.parse(partes[0]);
  double b = double.parse(partes[1]);
  double c = double.parse(partes[2]);

  double delta = (b * b) - (4 * a * c);

  if (a == 0 || delta < 0) {
    print("Impossivel calcular");
  } else {
    double r1 = (-b + sqrt(delta)) / (2 * a);
    double r2 = (-b - sqrt(delta)) / (2 * a);
    print("R1 = ${r1.toStringAsFixed(5)}");
    print("R2 = ${r2.toStringAsFixed(5)}");
  }
}