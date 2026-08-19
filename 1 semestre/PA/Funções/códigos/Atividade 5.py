from funcoes import nota

aluno_nota, tipo, media, op= 0.0, "", 0.0, ""

while True:
    notas= []
    for i in range(1,4):
        aluno_nota= float(input(f"Coloque a nota {i}: "))
        notas.append(aluno_nota)

    tipo= input("Coloque o tipo da média (A/P): ").strip().upper()
    while tipo not in ("A", "P"):
        tipo= input("Inválido. Digite A ou P: ").strip().upper()

    media= nota(notas[0], notas[1], notas[2], tipo)
    print(f"A média do aluno é {media:.2f}.")

    op= input("Deseja continuar? (s/n): ")
    if op.lower() != "s":
        break
