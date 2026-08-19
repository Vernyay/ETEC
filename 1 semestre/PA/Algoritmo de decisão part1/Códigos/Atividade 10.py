vcompra, vdesconto= 0.0, 0.0

vcompra= float(input("Coloque o valor da compra:"))

if vcompra>0 and vcompra<=100:
    vdesconto= vcompra*0.02
elif vcompra>100 and vcompra<=300:
    vdesconto= vcompra*0.05
elif vcompra>300 and vcompra<=700:
    vdesconto= vcompra*0.09
elif vcompra>700 and vcompra<=1200:
    vdesconto= vcompra*0.12
else:
    vdesconto= vcompra*0.15

print("Seu desconto é de:", vdesconto)
print("Sua compra foi de:", vcompra-vdesconto)