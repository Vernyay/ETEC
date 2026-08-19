vnum, vmedia, vcont= 0, 0, 0

while True:
    vnum= int(input(f"Coloque o {vcont+1}° número:"))
    if vnum<0:
        break
    vmedia+=vnum
    vcont+=1
vmedia= vmedia/vcont
print(f"A média desses números é {vmedia}")