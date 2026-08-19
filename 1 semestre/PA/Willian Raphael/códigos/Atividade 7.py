from funcoes import positivo

numero, op= 0, ""

while True:
    numero= int(input("Digite um valor: "))
    if positivo(numero):
        print(f"{numero} é positivo.")
    else:
        print(f"{numero} é negativo.")

    op= input("Deseja continuar? (s/n): ")
    if op.lower() != "s":
        break
