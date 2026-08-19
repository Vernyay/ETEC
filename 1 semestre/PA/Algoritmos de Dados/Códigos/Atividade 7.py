vlista, vnum, vmediaantes, vmediadepois= [], 0, 0, 0

for i in range(1,6):
    vnum= int(input(f"Coloque o {i} número: "))
    vlista.append(vnum)
    vmediaantes+=vnum
vmediaantes= vmediaantes/5
for i in range(6,11):
    vnum= int(input(f"Coloque o {i} número: "))
    vlista.append(vnum)
    vmediadepois+=vnum
vmediadepois= vmediadepois/5
print(f"A média dos 5 primeiros números é {vmediaantes}")
print(f"A média dos 5 últimos números é {vmediadepois}")