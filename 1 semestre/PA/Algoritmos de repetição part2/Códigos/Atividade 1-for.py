vnum, vsoma, vmedia, vcont= 0,0,0,0

for vcont in range(1,16):
    vnum= int(input(f"Coloque o {vcont}° número:"))
    vsoma+=vnum
vmedia=vsoma/15
print(f"A soma dos números é {vsoma}")
print(f"A média desses números é {vmedia}")