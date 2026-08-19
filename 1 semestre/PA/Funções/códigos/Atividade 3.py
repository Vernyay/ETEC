from funcoes import maior_num

num ,lista, op= 0, [], ""

while True:
    lista=[]
    for i in range(1,4):
        num= int(input(f"Digite o {i} número: "))
        lista.append(num)
    print(f"O maior número é: {maior_num(lista)}")
    op = str(input("Deseja continuar? (s/n): "))
    if op.lower() != "s":
        break