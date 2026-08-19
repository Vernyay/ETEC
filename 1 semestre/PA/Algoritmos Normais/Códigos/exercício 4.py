vcompra, vpercentual, vreaisdesconto, vnovovalor = 0.0, 0.0, 0.0, 0.0

vcompra= float(input("Digite o valor da compra: "))
vpercentual= float(input("Digite o valor do percentual de desconto: "))

vreaisdesconto= vcompra * (vpercentual / 100)
vnovovalor= vcompra - vreaisdesconto

print("O valor do desconto é: R$ ", vreaisdesconto)
print("O valor total da compra é: R$ ", vnovovalor)