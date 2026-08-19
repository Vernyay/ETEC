import 'dart:io';

void main()
{
  int temp = int.parse(stdin.readLineSync()!);
  int vel = int.parse(stdin.readLineSync()!);
  const consumo = 12;

  int dist = temp*vel;

  double gasto = dist/consumo;

  print('${gasto.toStringAsFixed(3)}');

}
