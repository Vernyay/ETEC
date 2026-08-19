vidade, vpeso, vmediaidade, vcontpeso, vcont= 0,0,0,0,0

while vcont<10:
    print("-" * 10)
    vpeso= float(input(f"Coloque o {vcont+1} peso:"))
    vidade= int(input(f"Coloque a {vcont+1}ª idade:"))
    vmediaidade+=vidade
    if vpeso>80:
        vcontpeso+=1
    vcont+=1
vmediaidade= vmediaidade/10
print(f"Tem {vcontpeso} pessoas com mais de 80 kg")
print(f"A média das idades é {vmediaidade}")