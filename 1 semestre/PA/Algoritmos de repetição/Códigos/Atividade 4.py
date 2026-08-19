vnum, vmediamaior, vmediamenor, vcont, vcontmaior, vcontmenor= 0, 0, 0, 0, 0, 0

while vcont<10:
    vnum= int(input(f"Coloque o {vcont+1}° número:"))
    if vnum>=10:
        vmediamaior+=vnum
        vcontmaior+=1
    else:
        vmediamenor+=vnum
        vcontmenor+=1
    vcont+=1
if vcontmaior>0:
    vmediamaior /= vcontmaior
    print(f"Média dos números maiores ou iguais a 10 são: {vmediamaior}")
else:
    print("Nenhum número maior ou igual a 10 foi digitado.")
if vcontmenor>0:
    vmediamenor /= vcontmenor
    print(f"Média dos números menores que 10 são: {vmediamenor}")
else:
    print("Nenhum número menor que 10 foi digitado.")


