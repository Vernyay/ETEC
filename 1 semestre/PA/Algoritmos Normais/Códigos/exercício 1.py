vprecogasolina, vodometroinicial, vodometrofinal, vgasolinagasta, vrecibopassageiro = 0.0, 0.0, 0.0, 0.0, 0.0

vprecogasolina=float(input("Digite o valor do litro da gasolina: "))
vodometroinicial=float(input("Digite o valor do odômetro no início da viagem: "))
vodometrofinal=float(input("Digite o valor do odômetro no final da viagem: "))
vgasolinagasta=float(input("Digite a quantidade de gasolina gasta na viagem: "))
vrecibopassageiro=float(input("Digite o valor recebido do passageiro: "))

vconsumogasolina= (vodometrofinal-vodometroinicial)/vgasolinagasta
vlucro= vrecibopassageiro-(vgasolinagasta*vprecogasolina)
print("O consumo de gasolina do carro é: ", vconsumogasolina, "km/l")
print("O lucro da viagem é: ", vlucro, "R$")