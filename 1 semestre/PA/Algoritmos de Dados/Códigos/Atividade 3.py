vlista, vmaior, vnum, vmaiornumero = [], 0, 0, float('-inf')
for i in range(1,11):
    vnum= int(input(f"Coloque o {i} número: "))
    vlista.append(vnum)
    if vnum>vmaiornumero:
        vmaiornumero=vnum
        vmaior=i
print(f"O maior número é {vmaiornumero} e está na posição {vmaior}")