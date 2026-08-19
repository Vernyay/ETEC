from funcoes import par

num=0

while True:
    num= int(input("Coloque o número para verificar: "))
    if num<0:
        break
    print(f"Esse número é par? {par(num)}")