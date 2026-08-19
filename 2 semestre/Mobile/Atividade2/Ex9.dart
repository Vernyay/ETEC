import 'dart:io';

void main()
{
    int func = int.parse(stdin.readLineSync()!);
    int hour = int.parse(stdin.readLineSync()!);
    double salar = double.parse(stdin.readLineSync()!);
    
    double payment = hour * salar;
    
    print('NUMBER = $func');
    print('SALARY = U\$ ${payment.toStringAsFixed(2)}');
}
