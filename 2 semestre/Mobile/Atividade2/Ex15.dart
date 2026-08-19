import 'dart:io';

void main()
{
  int X = int.parse(stdin.readLineSync()!);
  double Y = double.parse(stdin.readLineSync()!);

  double consumo = X/Y;

  print('${consumo.toStringAsFixed(3)} km/l');

}