vsexo, vidade, vmediamulher, vmediatodos, vmediahomens, vcontmulher, vconthomem, vcont= 0, 0, 0, 0, 0, 0, 0, 0

while vcont<12:
    print("-"*20)
    print(f"Pessoa {vcont+1}")
    print("-"*20)
    vsexo= int(input(f"Coloque o seu sexo, 1 para feminino e 2 para masculino:"))
    vidade= int(input("Coloque a sua idade:"))
    vmediatodos+=vidade
    if vsexo==1:
        vmediamulher+=vidade
        vcontmulher+=1
    else:
        vmediahomens+=vidade
        vconthomem+=1
    vcont+=1
vmediatodos= vmediatodos/12
vmediamulher= vmediamulher/vcontmulher
vmediahomens= vmediahomens/vconthomem
print(f"A média de todas as idades é {vmediatodos}")
print(f"A média das idades das mulheres é {vmediamulher}")
print(f"A média das idades dos homens é {vmediahomens}")