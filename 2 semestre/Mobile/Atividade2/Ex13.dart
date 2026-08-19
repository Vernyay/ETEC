import 'dart:io';

void main()
{
    List<String> line1 = stdin.readLineSync()!.split(' ');
    double A = double.parse(line1[0]);
    double B = double.parse(line1[1]);
    double C = double.parse(line1[2]);
    
    double Area_Triangulo = (A*C)/2;
    double Area_Circulo = 3.14159*(C*C);
    double Area_Trapezio = ((A+B)*C)/2;
    double Area_Quadrado = B*B;
    double Area_Retangulo = A*B;
    
    print('TRIANGULO: ${Area_Triangulo.toStringAsFixed(3)}');
    print('CIRCULO: ${Area_Circulo.toStringAsFixed(3)}');
    print('TRAPEZIO: ${Area_Trapezio.toStringAsFixed(3)}');
    print('QUADRADO: ${Area_Quadrado.toStringAsFixed(3)}');
    print('RETANGULO: ${Area_Retangulo.toStringAsFixed(3)}');
}

