import 'dart:io';

void main(){
    List<String> frutas = [];
    print('==== Programa da Feira =====');
    print('Quantas frutas deseja compra?');
    int numeroFrutas = int.parse(stdin.readLineSync()!);
    for (int i = 0; i < numeroFrutas; i++){
        print("Digite o nome da fruta comprada: ");
        String frutaComprada = stdin.readLineSync()!.toLowerCase();
        frutas.add(frutaComprada);
    }
    if (frutas.isNotEmpty) {
    print('\nPrimeira fruta cadastrada: ${frutas.first}');
    }
    print('Deseja remover alguma fruta? (sim/não)');
    String resposta = stdin.readLineSync()!.toLowerCase();

    if (resposta=="sim"){
        print("Digite o nome da fruta que deseja remover: ");
        String frutaRemovida = stdin.readLineSync()!;toLowerCase();
        if (frutas.isEmpty) {
            print("A cesta está vazia!");
        } else if (fruta.contains(frutaRemovida)){
            frutas.remove(frutaRemovida);
            print("Fruta removida com sucesso!");
        } else {
            print("Essa fruta não está na lista.");
        }
    }
    print('\nQuantidade de frutas restantes: ${frutas.length}');
    print('Frutas na sua cesta: $frutas');

    //não sei se é necessario, mas ta aí a ultima instrução

    print('\n=== Percorrendo a lista com For-In ===');
    for (var fruta in frutas) {
    print('- $fruta');
    }

    print('\n=== Percorrendo a lista com While ===');
    int contador = 0;
    while (contador < frutas.length) {
        print('- ${frutas[contador]}');
        contador++;
    }
}