vnota, vcontruim, vcontrazoavel, vcontsatisfatorio, vcontbom, vcontotimo, vcondicao= 0,0,0,0,0,0, "SIM"

while vcondicao!='NAO'.capitalize().strip():
    vnota= int(input("Avalie sua experiência: 1-Ruim, 2-Razoável, 3-Satisfatório, 4-Bom, 5-Ótimo"))
    if vnota == 1:
        vcontruim += 1
    elif vnota == 2:
        vcontrazoavel += 1
    elif vnota == 3:
        vcontsatisfatorio += 1
    elif vnota == 4:
        vcontbom += 1
    elif vnota == 5:
        vcontotimo += 1
    else:
        print("Nota inválida! Por favor, digite uma nota de 1 a 5.")
        continue
    vcondicao= str(input("Deseja continuar? digite 'SIM' para continuar e 'NAO' para acabar:")).capitalize().strip()
print("--- RESULTADO FINAL DA CONSULTA ---")
print(f"Quantidade de notas Ruim (1): {vcontruim}")
print(f"Quantidade de notas Razoável (2): {vcontrazoavel}")
print(f"Quantidade de notas Satisfatório (3): {vcontsatisfatorio}")
print(f"Quantidade de notas Bom (4): {vcontbom}")
print(f"Quantidade de notas Ótimo (5): {vcontotimo}")