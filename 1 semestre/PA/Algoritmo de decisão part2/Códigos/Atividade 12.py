vbonus, vsalario, vtemposervico= 0.0,0.0,0.0

vsalario = float(input("Salário: "))
vtemposervico = int(input("Anos na empresa: "))

if vtemposervico >= 5:
    vbonus = vsalario * 0.20
else:
    vbonus = vsalario * 0.10

print("Bônus recebido: R$", vbonus)