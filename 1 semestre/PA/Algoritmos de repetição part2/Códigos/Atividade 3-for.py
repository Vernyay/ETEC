vnum, vcont10, vcontentre, vcontmenores, vcont= 0, 0, 0, 0, 0

for vcont in range(1,11):
    vnum= int(input(f"Coloque o {vcont}° número:"))
    if vnum>10:
        vcont10+=1
    if vnum<5:
        vcontmenores+=1
    if vnum>7 and vnum<=15:
        vcontentre+=1
print(f"Existe {vcont10} números maiores que 10")
print(f"Existe {vcontentre} números entre 7 e 15")
print(f"Existe {vcontmenores} números menores que 5")