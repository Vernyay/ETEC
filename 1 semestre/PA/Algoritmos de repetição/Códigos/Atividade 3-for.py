vnum, vcont, vmaior, vmenor= 0, 0, 0, 0

for vcont in range(1,16):
    vnum= int(input(f"Coloque o {vcont+1}° número:"))
    if vmaior==0 and vmenor==0:
        vmaior=vnum
        vmenor=vnum
    else:
        if vnum>vmaior:
            vmaior=vnum
        if vnum<vmenor:
            vmenor=vnum

print(f"O maior número é: {vmaior}")
print(f"O menor número é: {vmenor}")