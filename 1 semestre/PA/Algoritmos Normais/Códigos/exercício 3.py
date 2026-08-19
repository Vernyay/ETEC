vcarros, vvendas, vtotal, vsalariofixo = 0.0, 0.0, 0.0, 0.0

vsalariofixo= float(input("Digite o valor do salário fixo: "))
vcarros= float(input("Digite o valor total de carros vendidos: "))
vvendas= float(input("Digite o valor total de vendas: "))

vtotal= (2 * vsalariofixo) + (50 * vcarros) + (vvendas * 5 / 100)
print("O valor total do salario desse vendedor é: R$ ", vtotal)