vlista, vnum, vpar, vimpar= [], 0, 0 , 0

for i in range(1,21):
    vnum= int(input(f"Coloque o {i} número:"))
    vlista.append(vnum)
    if vnum%2==0:
        vpar+=1
    else:
        vimpar+=1
print(f"A quantidade de números pares é {vpar}")
print(f"A quantidade de números impares é {vimpar}")