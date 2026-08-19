vmaiorvalturamulher, vmenorvalturahomem, vtevemulher, vtevehomem, valtura, vsexo, i= 0, 0, False, False, 0, 0, 0

vmenorvalturahomem = 3.0

for i in range(1, 21):
    print(f"--- Dados da {i}ª Pessoa ---")
    valtura = float(input("Digite a valtura (ex: 1.75): "))
    print("Sexo: 1 - Mulher | 2 - Homem")
    vsexo = int(input("Digite o código do vsexo: "))

    if vsexo == 1:
        vtevemulher = True
        if valtura > vmaiorvalturamulher:
            vmaiorvalturamulher = valtura
            
    elif vsexo == 2:
        vtevehomem = True
        if valtura < vmenorvalturahomem:
            vmenorvalturahomem = valtura
    else:
        print("Código de vsexo inválido! Dados ignorados para este cálculo.")

print("\n" + "="*30)
print("RESULTADOS DA PESQUISA")
print("="*30)

if vtevemulher:
    print(f"A maior mulher tem: {vmaiorvalturamulher:.2f}m")
else:
    print("Não foram registradas mulheres no grupo.")

if vtevehomem:
    print(f"O menor homem tem: {vmenorvalturahomem:.2f}m")
else:
    print("Não foram registrados homens no grupo.")