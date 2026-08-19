import 'dart:io';

void main()
{
    int diasT = int.parse(stdin.readLineSync()!);

    int anos = diasT ~/ 365;
    int restoDias = diasT % 365;
    int meses = restoDias ~/ 30;
    int dias = restoDias % 30;

    print('$anos ano(s)');
    print('$meses mes(es)');
    print('$dias dia(s)');
}
