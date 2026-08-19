vdias, vkmrodado, vtotal = 0.0, 0.0, 0.0

vkmrodado= float(input("Digite quanto que seu carro percorreu em quilômetros: "))
vdias= int(input("Digite quantos dias você ficou com o carro: "))

vtotal= (vkmrodado*2.2) + (vdias*90)
print("O valor total a ser pago é de: R$ ", vtotal)