vbruto, vfgts, vinssv, vir, vliquido, vqtdh, vsind, vvalorh, vtotaldesc= 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0

vvalorh = float(input("Valor da hora: "))
vqtdh = float(input("Horas trabalhadas: "))
vbruto = vvalorh * vqtdh

if vbruto <= 900: 
    vir = 0
elif vbruto <= 1500: 
    vir = vbruto * 0.05
elif vbruto <= 2500: 
    vir = vbruto * 0.10
else: 
    vir = vbruto * 0.20

vsind = vbruto * 0.03
vinss = vbruto * 0.10
vfgts = vbruto * 0.01
vtotaldesc = vir + vsind + vinss
vliquido = vbruto - vtotaldesc 

print("Salário Bruto: R$", vbruto)
print("(-) IR: R$", vir)
print("(-) Sindicato: R$", vsind)
print("(-) INSS: R$", vinss)
print("FGTS: R$", vfgts)
print("Total de descontos: R$", vtotaldesc)
print("Salário Líquido: R$", vliquido)