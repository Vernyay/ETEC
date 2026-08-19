vemprestimo, vnparcelas, vparcela, vsalario, vtotal= 0.0,0.0,0.0,0.0,0.0

vemprestimo = float(input("Valor empréstimo: "))
vnparcelas = int(input("Parcelas: "))
vsalario = float(input("Salário: "))

vtotal = vemprestimo * 1.10
vparcela = vtotal / vnparcelas

if vparcela <= (vsalario * 0.30):
    print("Empréstimo APROVADO")
else:
    print("Empréstimo NEGADO")