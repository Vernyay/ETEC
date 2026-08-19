vprecolitro, vsaldo, vrecebeu = 0.0, 0.0, 0.0

vprecolitro = float(input("Digite o valor do litro de combustível: "))
vsaldo = float(input("Digite o valor do saldo disponível: "))

vrecebeu= vsaldo / vprecolitro
print("Ele recebeu: ", vrecebeu, "litros de combustível")