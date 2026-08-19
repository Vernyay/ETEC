v_lado1, v_lado2, v_lado3= 0.0,0.0,0.0

v_lado1 = float(input("Lado 1: "))
v_lado2 = float(input("Lado 2: "))
v_lado3 = float(input("Lado 3: "))

if v_lado1 + v_lado2 > v_lado3 and v_lado1 + v_lado3 > v_lado2 and v_lado2 + v_lado3 > v_lado1:
    if v_lado1 == v_lado2 == v_lado3:
        print("Equilátero")
    elif v_lado1 == v_lado2 or v_lado1 == v_lado3 or v_lado2 == v_lado3:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não formam um triângulo.")