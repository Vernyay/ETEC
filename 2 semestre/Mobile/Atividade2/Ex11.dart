import 'dart:io';

void main()
{
    List<String> line1 = stdin.readLineSync()!.split(' ');
    int code1 = int.parse(line1[0]);
    int quantity1 = int.parse(line1[1]);
    double priceUnit1 = double.parse(line1[2]);
    
    List<String> line2 = stdin.readLineSync()!.split(' ');
    int code2 = int.parse(line2[0]);
    int quantity2 = int.parse(line2[1]);
    double priceUnit2 = double.parse(line2[2]);
    
    double total = (quantity1*priceUnit1)+(quantity2*priceUnit2);
    
    print('VALOR A PAGAR: R\$ ${total.toStringAsFixed(2)}');
}

