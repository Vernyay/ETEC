vpessoa, i, vmaiorsalario, vfilho, vmediasalario, vsalario, vmediafilho, vsalario1200= 0, 0, 0, 0, 0, 0, 0

for i in range(1,21):
    print(f"---Pessoa {i}---")
    vsalario= float(input("Coloque o valor do seu salário:"))
    vfilho= int(input("Coloque a quantidade de filhos:"))
    vmediasalario+=vsalario
    vmediafilho+=vfilho
    if vsalario>vmaiorsalario:
        vmaiorsalario=vsalario
    if vsalario<1200:
        vsalario1200+=1
vmediasalario= vmediasalario/20
vmediafilho= vmediafilho/20
vsalario1200=(vsalario1200*100)/20
print(f"A media do salário da população é R${vmediasalario}")
print(f"A media de filhos da população é {vmediafilho}")
print(f"O maior salário é {vmaiorsalario}")
print(f"O percentual de pessoas com um salário até R$1200 é {vsalario1200}")