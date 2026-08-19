import 'dart:io';

void main()
{
    String name = (stdin.readLineSync()!);
    double fixed = double.parse(stdin.readLineSync()!);
    double sold = double.parse(stdin.readLineSync()!);
    
    double reajust = (sold*0.15)+fixed;
    
    print('TOTAL = R\$ ${reajust.toStringAsFixed(2)}');
}
