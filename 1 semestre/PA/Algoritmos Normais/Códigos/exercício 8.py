vcomprimento, vlargura, varea, vvalormercado, vtotal = 0.0, 0.0, 0.0, 0.0, 0.0

vlargura= float(input("Digite a largura do terreno: "))
vcomprimento= float(input("Digite o comprimento do terreno: "))
vvalormercado= float(input("Digite o valor do metro quadrado: "))

varea= vlargura * vcomprimento
vtotal= varea * vvalormercado

print("A área do terreno é: ", varea, "metros quadrados")
print("O valor total do terreno é: R$ ", vtotal)