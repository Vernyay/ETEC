import random
vlistaaleatoria, vnumerosorteado, vpalpite= [], 0, 0

for i in range(20):
    vnumerosorteado = random.randint(1, 50)
    vlistaaleatoria.append(vnumerosorteado)

vpalpite = int(input("Digite um número inteiro para buscar na lista: "))


if vpalpite in vlistaaleatoria:
    print(f"O número {vpalpite} EXISTE dentro da lista!")
else:
    print(f"O número {vpalpite} NÃO EXISTE dentro da lista.")

print(f"\nLista completa gerada: {vlistaaleatoria}")