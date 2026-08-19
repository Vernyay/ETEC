vsomaidadeotimo, vqtdotimo, vqtdregular, vqtdbom, vidade, vopiniao, vmediaotimo, vpercentagembom, i= 0, 0, 0, 0, 0, 0, 0, 0, 0


for i in range(1, 16):
    print(f"--- Espectador {i} ---")
    vidade = int(input("Digite a vidade: "))
    
    print("Opiniões: 3 - Ótimo | 2 - Bom | 1 - Regular")
    vopiniao = int(input("Digite a sua opinião: "))
    
    if vopiniao == 3:
        vsomaidadesotimo += vidade
        vqtdotimo += 1
    elif vopiniao == 2:
        vqtdbom += 1
    elif vopiniao == 1:
        vqtdregular += 1
    else:
        print("Opção inválida! Este voto não será contabilizado.")

if vqtdotimo > 0:
    vmediaotimo = vsomaidadesotimo / vqtdotimo
else:
    vmediaotimo = 0

vpercentagembom = (vqtdbom / 15) * 100

print("\n" + "="*30)
print("RELATÓRIO FINAL")
print("="*30)

if vqtdotimo > 0:
    print(f"A) Média de vidade (Ótimo): {vmediaotimo:.1f} anos")
else:
    print("A) Média de vidade (Ótimo): Nenhuma pessoa respondeu ótimo.")

print(f"B) Quantidade de pessoas (Regular): {vqtdregular}")
print(f"C) Percentagem de pessoas (Bom): {vpercentagembom:.1f}%")