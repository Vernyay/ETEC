import 'dart:io';

void main()
{
    int temp = int.parse(stdin.readLineSync()!);

    int horas = temp ~/ 3600;
    int resto = temp % 3600;
    int minutos = resto ~/ 60;
    int segundos = resto % 60;

    
    print('$horas:$minutos:$segundos');
}
