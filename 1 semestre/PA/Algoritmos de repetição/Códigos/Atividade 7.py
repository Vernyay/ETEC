vcont, vaprovados, vreprovados, vmedia = 0, 0, 0, 0

while vcont < 10:
    print(f"--- Aluno {vcont + 1} ---")
    vcontnota = 0
    vmedia = 0
    while vcontnota < 4:
        vnota = float(input(f"Coloque a {vcontnota + 1}° nota: "))
        vmedia += vnota
        vcontnota += 1
        
    vmedia /= 4
    print(f"A média desse aluno é: {vmedia:.2f}")
    
    if vmedia >= 7:
        print("Situação: Aprovado")
        vaprovados += 1
    else:
        print("Situação: Reprovado")
        vreprovados += 1
    
    vcont += 1


print(f"Total de aprovados: {vaprovados}")
print(f"Total de reprovados: {vreprovados}")