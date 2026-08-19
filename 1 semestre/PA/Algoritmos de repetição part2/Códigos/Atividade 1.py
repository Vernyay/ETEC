vnum, vsoma, vmedia, vcont= 0,0,0,0

while vcont<15:
    vnum= int(input(f"Coloque o {vcont+1}° número:"))
    vsoma+=vnum
    vcont+=1
vmedia=vsoma/15
print(f"A soma dos números é {vsoma}")
print(f"A média desses números é {vmedia}")