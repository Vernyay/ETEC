vnum, vsomapares, vsomaimpares, vcont= 0, 0, 0, 0

while vcont<10:
    vnum= int(input(f"Coloque o {vcont+1}° número : "))
    if vnum%2==0:
        vsomapares+=vnum
    else:
        vsomaimpares+=vnum
    vcont+=1
print(f"A soma dos ímpares é {vsomaimpares}")
print(f"A soma dos pares é {vsomapares}")