vano, vimposto, vvalorcarro= 0.0,0.0,0.0

vano = int(input("Ano do carro: "))
vvalorcarro = float(input("Valor de tabela: "))

if vano < 2000:
    vimposto = vvalorcarro * 0.01
else:
    vimposto = vvalorcarro * 0.015

print("Valor do imposto: R$", vimposto)