vmatriz, vsoma = [], 0

for i in range(3):
    vlinha = []
    for j in range(3):
        vnum = int(input(f"Digite o valor para [{i}][{j}]: "))
        vlinha.append(vnum)
    vmatriz.append(vlinha)

for i in range(3):
    for j in range(3):
        if i < j:
            vsoma += vmatriz[i][j]
print(f"A vsoma dos números acima da diagonal principal é: {vsoma}")