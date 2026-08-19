valtura, vlargura, varea, vconsguepintar, vlatas = 0.0, 0.0, 0.0, 0.0, 0.0

vlargura= float(input("Digite a largura da parede em metros: "))
valtura= float(input("Digite a altura da parede em metros: "))
vconsguepintar= float(input("Digite a quantidade de metros quadrados que uma lata consegue pintar: "))

varea= vlargura * valtura
vlatas= varea / vconsguepintar

print("A área da parede é: ", varea, "metros quadrados")
print("A quantidade de latas necessárias para pintar a parede é: ", vlatas)