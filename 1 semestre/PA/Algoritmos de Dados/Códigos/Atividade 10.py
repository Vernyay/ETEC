vlistanumeros, vsoma, vnum, vmedia= [], 0, 0, 0

for i in range(1, 21):
    vnum = float(input(f"Digite o {i}º número: "))
    vlistanumeros.append(vnum)

for vnum in vlistanumeros:
    vsoma += vnum

vmedia = vsoma / 20

print(f"A média de todos os números é: {vmedia:.2f}")
print("Os números maiores que a média são:")

for vnum in vlistanumeros:
    if vnum > vmedia:
        print(f"-> {vnum}")