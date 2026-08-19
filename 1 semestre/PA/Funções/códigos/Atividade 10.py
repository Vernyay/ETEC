from funcoes import reajuste_salario

salario, filhos, salario_ref, indice= 0.0, 0, [], 0

while True:
    salario = float(input("Digite o salário do funcionário: "))
    filhos = int(input("Digite o número de filhos: "))

    if salario<0 or filhos<0:
        break

    salario_ref = [salario]
    indice = reajuste_salario(salario_ref, filhos)

    print(f"Índice de reajuste: {indice}%")
    print(f"Novo salário: R$ {salario_ref[0]:.2f}")