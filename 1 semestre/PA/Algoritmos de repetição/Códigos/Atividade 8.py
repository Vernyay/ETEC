vn1, vn2, vcont, vblabla, vsoma, vnatual= 0, 0, 0, 0, 0, 0

vn1= int(input("Coloque o primeiro número:"))
vn2= int(input("Coloque o segundo número:"))

if vn1>vn2:
    vblabla=vn1
    vn1=vn2
    vn2=vblabla

vnatual=vn1

while vnatual<=vn2:
    vsoma+=vnatual
    vnatual+=1

print(f"A soma total é: {vsoma}")