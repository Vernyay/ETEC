vlistanumeros, vsomaate20, vsoma21a30, vsomamaior30, vnum= [], 0, 0, 0, 0

for i in range(1, 11):
    vnum = int(input(f"Digite o {i}º número inteiro: "))
    vlistanumeros.append(vnum)
for vnum in vlistanumeros:
    if vnum <= 20:
        vsomaate20 += vnum
    elif vnum <= 30:
        vsoma21a30 += vnum
    else:
        vsomamaior30 += vnum
print(f"a) Soma dos números até 20 (inclusive): {vsomaate20}")
print(f"b) Soma dos números entre 21 e 30 (inclusive): {vsoma21a30}")
print(f"c) Soma dos números maiores que 30: {vsomamaior30}")