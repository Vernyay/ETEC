vlista, vnegativo, vpositivos, vcontpositivos, vnum= [], 0, 0, 0, 0

for i in range(1,21):
    vnum= int(input(f"Coloque o {i} número: "))
    vlista.append(vnum)
    if vnum<0:
        vnegativo+=1
    else:
        vpositivos+=vnum
        vcontpositivos+=1

if vcontpositivos > 0:
    vpositivos = vpositivos / vcontpositivos
else:
    vpositivos = 0

print(f"A quantidade de números negativos é: {vnegativo}")
print(f"A média dos números positivos é: {vpositivos}")