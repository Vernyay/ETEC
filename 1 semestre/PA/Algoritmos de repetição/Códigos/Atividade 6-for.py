vnum, vmedia, vcont, vmaior, vmenor, vsomainter, vsomatotal= 0, 0, 0, 0, 0, 0, 0

for vcont in range(1,6):
    vnum= int(input(f"Coloque o {vcont+1}° número:"))
    vsomatotal+=vnum
    if vnum>vmaior or vmaior==0:
        vmaior=vnum
    if vnum<vmenor or vmenor==0:
        vmenor=vnum
    vsomainter= (vsomatotal-vmaior)-vmenor
    vmedia= vsomainter/3

print(f"A média dos intermediários é: {vmedia}")