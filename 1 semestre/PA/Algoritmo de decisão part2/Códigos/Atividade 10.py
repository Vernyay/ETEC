vsalbase, vperc, vaumento, vsalnovo= 0.0,0.0,0.0,0.0

vsalbase = float(input("Salário atual: "))

if vsalbase <= 1000: 
    vperc = 0.20
elif vsalbase <= 1500 and vsalbase > 1000: 
    vperc = 0.15
elif vsalbase <= 2500 and vsalbase > 1500: 
    vperc = 0.10
else: 
    vperc = 0.05

vaumento = vsalbase * vperc
vsalnovo = vsalbase + vaumento

print("Salário antes: R$", vsalbase)
print("Percentual: ", vperc * 100, "%")
print("Valor aumento: R$", vaumento)
print("Novo salário: R$", vsalnovo)