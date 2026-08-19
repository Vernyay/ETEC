vcont, vaprovados, vreprovados, vmedia = 0, 0, 0, 0

for vcont in range(1,11):
    print(f"--- Aluno {vcont} ---")
    vcontnota = 0
    vmedia = 0
    for vcontnota in range(1,5):
        vnota = float(input(f"Coloque a {vcontnota}° nota: "))
        vmedia += vnota
        
    vmedia /= 4
    print(f"A média desse aluno é: {vmedia:.2f}")
    
    if vmedia >= 7:
        print("Situação: Aprovado")
        vaprovados += 1
    else:
        print("Situação: Reprovado")
        vreprovados += 1


print(f"Total de aprovados: {vaprovados}")
print(f"Total de reprovados: {vreprovados}")