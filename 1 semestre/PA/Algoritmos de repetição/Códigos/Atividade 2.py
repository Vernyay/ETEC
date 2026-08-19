vnum, vsoma, vcont= 0, 0, 0

while vnum>=0:
    vnum= int(input(f"Coloque o {vcont+1}° número:"))
    if vnum<0:
        break
    else:
        vsoma+=vnum
        vcont+=1

print(f"A soma dos números é {vsoma}")