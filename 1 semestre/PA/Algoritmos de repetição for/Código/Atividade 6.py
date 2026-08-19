vsomaidades, vtotalpessoas, vidade, vmedia, i= 0, 0, 0, 0, 0

for i in range(1, 21):
    vidade = int(input(f"Digite a vidade da {i}ª pessoa: "))
    vsomaidades += vidade

vmedia = vsomaidades / vtotalpessoas

print("-" * 30)
print(f"A média das idades é: {vmedia:.1f} anos")