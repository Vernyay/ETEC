vfaixa1, vfaixa2, vfaixa3, vfaixa4, vfaixa5, vidade, i, vpercprimeira, vpercultima= 0, 0, 0, 0, 0, 0, 0, 0, 0

for i in range(1, 16):
    vidade = int(input(f"Digite a vidade da {i}ª pessoa: "))
    
    if vidade <= 15:
        vfaixa1 += 1
    elif vidade <= 30:
        vfaixa2 += 1
    elif vidade <= 45:
        vfaixa3 += 1
    elif vidade <= 60:
        vfaixa4 += 1
    else:
        vfaixa5 += 1

vpercprimeira = (vfaixa1 / 15) * 100
vpercultima = (vfaixa5 / 15) * 100

print("-" * 30)
print("QUANTvIDADE POR FAIXA ETÁRIA:")
print(f"Até 15 anos: {vfaixa1}")
print(f"De 16 a 30 anos: {vfaixa2}")
print(f"De 31 a 45 anos: {vfaixa3}")
print(f"De 46 a 60 anos: {vfaixa4}")
print(f"Acima de 61 anos: {vfaixa5}")

print("-" * 30)
print("PERCENTAGENS:")
print(f"Pessoas na 1ª faixa (até 15 anos): {vpercprimeira:.2f}%")
print(f"Pessoas na última faixa (acima de 61 anos): {vpercultima:.2f}%")