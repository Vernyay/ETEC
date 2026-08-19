int1, int2= 0, 0

int1= int(input("Coloque o primeiro numero: "))
int2= int(input("Coloque o segundo numero: "))
if int1==int2:
    print("Os numeros são iguais")
else:
    if int1>int2:
        print("O numero maior é: ", int1)
    else:
        print("O numero maior é: ", int2)