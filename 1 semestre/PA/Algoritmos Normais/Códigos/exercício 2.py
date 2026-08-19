vpeso, vquantidade, vresto = 0.0, 0.0, 0.0

vpeso=float(input("Digite o peso do pacote em quilogramas: "))
vquantidade=float(input("Digite a quantidade de ração dada para cada gato em gramas: "))

vresto= vpeso-((vquantidade/1000)*2*5)

print("O peso restante do pacote de ração é: ", vresto, "kg")