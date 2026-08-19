import 'dart:io';

void main()
{
    List<String> line1 = stdin.readLineSync()!.split(' ');
    int A = int.parse(line1[0]);
    int B = int.parse(line1[1]);
    int C = int.parse(line1[2]);
    
    int maiorAB = (A+B+(A-B).abs()) ~/ 2;
    int maiorEnd = (maiorAB+C+(maiorAB-C).abs()) ~/ 2;

    print('$maiorEnd eh o maior');
}

