vnum1,vnum2,vnum3=0,0,0

vnum1=int(input("Digite o primeiro número: "))
vnum2=int(input("Digite o segundo número: "))
vnum3=int(input("Digite o terceiro número: "))

if vnum1 == vnum2 == vnum3:
    print("Todos os números são iguais.")
elif vnum1 == vnum2:
    print("Dois números são iguais.", vnum1)
    if vnum1 > vnum3:
        print("Eles são maiores que:", vnum3)
    else:
        if vnum1 < vnum3:
            print("Eles são menores que:", vnum3)
elif vnum2 == vnum3:
    print("Dois números são iguais.", vnum2)
    if vnum2 > vnum1:
        print("Eles são maiores que:", vnum1)
    else:
        if vnum2 < vnum1:
            print("Eles são menores que:", vnum1)
elif vnum1 == vnum3:
    print("Dois números são iguais.", vnum1)
    if vnum1 > vnum2:
        print("Eles são maiores que:", vnum2)
    else:
        if vnum1 < vnum2:
            print("Eles são menores que:", vnum2)
else:
    if vnum1 > vnum2 and vnum1 > vnum3:
        print(vnum1, "é o maior número.")
    elif vnum2 > vnum1 and vnum2 > vnum3:
        print(vnum2, "é o maior número.")
    else:
        print(vnum3, "é o maior número.")
    if vnum1 < vnum2 and vnum1 < vnum3:
        print(vnum1, "é o menor número.")
    elif vnum2<vnum1 and vnum2<vnum3:
        print(vnum2, "é o menor número.")
    else:
        print(vnum3, "é o menor número.")