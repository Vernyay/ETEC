from funcoes import fatorial

num= 0

while True:
    num = int(input("Digite um valor inteiro e positivo: "))
    if num<0:
        break
    print(f"O fatorial de {num} é {fatorial(num)}")
