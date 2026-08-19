vmatriz, vmaiores = [], 0

for i in range(3):
    vlinha = []
    for j in range(3):
        vnum= int(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))
        vlinha.append(vnum)
    vmatriz.append(vlinha)

for i in range(3):
    for j in range(3):
        if vmatriz[i][j]>10:
            vmaiores+=1
print(f"Quantidade de números maiores que 10: {vmaiores}")