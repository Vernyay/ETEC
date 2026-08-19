i, vsexo, valtura, vmediamulheres, vmaior, vmenor, vmediatotal, vcontmulher= 0, 0, 0, 0, 0, 0, 0, 0

for i in range(1,51):
    print(f"---Pessoa {i}---")
    vsexo= int(input("Coloque seu sexo: 1 para masculino e 2 para feminino"))
    valtura= float(input("Coloque a sua altura em metros:"))
    vmediatotal+=valtura
    if valtura>vmaior:
        vmaior=valtura
    if valtura<vmenor:
        vmenor=valtura
    if vsexo==2:
        vmediamulheres+=valtura
        vcontmulher+=1
vmediatotal= vmediatotal/50
vmediamulheres= vmediamulheres/vcontmulher
print(f"A maior altura é {vmaior}")
print(f"A menor altura é {vmenor}")
print(f"A média de todas as alturas é {vmediatotal}")
print(f"A média das alturas de todas as mulheres é {vmediamulheres}")