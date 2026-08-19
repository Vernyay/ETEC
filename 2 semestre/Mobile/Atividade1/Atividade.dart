import "dart:io";

void main() {
  int valor = int.parse(stdin.readLineSync()!);
  int number = valor;
  if (number>0 && number<1000000) {
    //Calcula a quantidade de notas de 100 reais
    int cem = valor ~/ 100;
    valor %=100; 
    int cinq = valor ~/ 50;
    valor %= 50;
    int vint = valor ~/ 20;
    valor %= 20;
    int dez = valor ~/ 10;
    valor %= 10;
    int cinc = valor ~/ 5;
    valor %= 5;
    int dois = valor ~/ 2;
    valor %= 2;
    int um = valor ~/ 1;
    valor %= 1;

    print("$cem nota(s) de R\$100");
    print("$cinq nota(s) de R\$50");
    print("$vint nota(s) de R\$20");
    print("$dez nota(s) de R\$10");
    print("$cinc nota(s) de R\$5");
    print("$dois nota(s) de R\$2");
    print("$um nota(s) de R\$1");

  } else {
    print("Presentention Error!");
  }
  
}