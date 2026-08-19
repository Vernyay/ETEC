vsoma, vmaior, vmenor, i, vnum, vmedia= 0, 0, 0, 0, 0, 0

for i in range(1, 21):
    vnum = int(input(f"Digite o {i}º número inteiro: "))
    
    vsoma += vnum

    if vnum > vmaior:
        vmaior = vnum
        
    if vnum <= vmenor:
        vmenor = vnum

vmedia = vsoma / 20

print("\n" + "="*30)
print(f"Maior número digitado: {vmaior}")
print(f"Menor número digitado: {vmenor}")
print(f"Média dos números: {vmedia:.2f}")
print("="*30)