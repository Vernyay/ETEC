vlista, vnum, vcheck, vpos= [], 0, 0, 0

for i in range(20):
    vnum= int(input("Coloque um número: "))
    vlista.append(vnum)

vcheck= int(input("Verifique um número se está na lista: "))


if vcheck in vlista:
    vpos= vlista.index(vcheck)
    print(f"Ele está na lista!!! Está na posição: {vpos}")
else: 
    print("Ele não está na lista!!!")