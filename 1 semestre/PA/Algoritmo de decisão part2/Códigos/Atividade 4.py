v_custo, v_venda= 0.0,0.0

v_custo = float(input("Valor da compra: "))

if v_custo < 20:
    v_venda = v_custo * 1.45
else:
    v_venda = v_custo * 1.30

print("Valor de venda: R$", v_venda)

#igual a anterior