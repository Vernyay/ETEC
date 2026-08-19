vnum, vsomapares, vsomaimpares, vcont= 0, 0, 0, 0

for vcont in range(1,11):
    vnum= int(input(f"Coloque o {vcont}° número : "))
    if vnum%2==0:
        vsomapares+=vnum
    else:
        vsomaimpares+=vnum
print(f"A soma dos ímpares é {vsomaimpares}")
print(f"A soma dos pares é {vsomapares}")