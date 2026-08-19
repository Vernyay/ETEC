import 'dart:io';

void main()
{
    const pi = 3.14159;
    double raio = double.parse(stdin.readLineSync()!);
    double form = (4.0/3)*pi*(raio*raio*raio);
    
    print('VOLUME = ${form.toStringAsFixed(3)}');
}
