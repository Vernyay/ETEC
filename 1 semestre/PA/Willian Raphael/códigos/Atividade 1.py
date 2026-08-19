from funcoes import soma

salario, reajuste, somar= 0.0, 0.0, 0.0

while True:
    print("Digite um número negativo em qualquer campo para sair do programa")
    salario= float(input("Coloque seu salario: "))
    reajuste= float(input("Coloque o valor do reajuste: "))
    if salario < 0 or reajuste < 0:
        break
    somar= soma(salario, reajuste)
    print(f"O salário desse funcionário reajustado é R${somar}!!!")
    if somar<1400:
        print("Salário abaixo da média!!!")
    elif somar>=1400 and somar<=1800:
        print("Salário dentro da média!!!")
    else:
        print("Salário acima da média!!!")