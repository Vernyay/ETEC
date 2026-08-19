import "dart:io";

void main() {
  var list = [];
  print("Coloque um número: ")
  for (i = 1; i < 3; i++) {
    int numer = int.parse(stdin.readLineSync()!);
    list.add(numer);
  }
  int big = list[0];
  for (i=0; i< list.lenght; i++) {
    if (list[i] > big) {
      big = list[i];
    }
  }
  print('O maior numero deles é: $big') 
}