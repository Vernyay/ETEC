from funcoes import categoria

idade= 0

while True: 
    idade= int(input("Digite sua idade: "))
    if idade<0:
        break
    print(categoria(idade))