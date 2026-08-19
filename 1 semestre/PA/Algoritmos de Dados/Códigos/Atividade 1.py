vnota, vmedia, vlista= 0, 0, []

for i in range(1,6):
    vlista.append(int(input(f"Entre com a {i}ª nota: ")))
for i in range(5):
    vnota += vlista[i]
vmedia= vnota/5

print(f"A média do aluno é :{vmedia}")

if vmedia >= 7:
    print("Aluno Aprovado!!!")
elif vmedia >= 5: 
    print("Aluno em recuperação!!!")
else:
    print("Aluno Reprovado!!!")