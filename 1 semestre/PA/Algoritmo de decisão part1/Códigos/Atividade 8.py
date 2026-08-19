vpreco, vtaxa, vestado= 0.0, 0.0, ""

vpreco=  float(input("Coloque o valor da venda:"))
vestado= str(input("Coloque a sigla do seu estado:")).strip().upper()

if vestado=="SP":
    vtaxa= vpreco*0.25
elif vestado=="RJ":
    vtaxa= vpreco*0.18
elif vestado=="PR":
    vtaxa= vpreco*0.15
elif vestado=="SC":
    vtaxa= vpreco*0.12
else:
    print("Estado não cadastrado!!!")
    vtaxa= -1

if vtaxa != -1:
    vpreco+=vtaxa
    print("Valor do imposto no seu estado:", vtaxa)
    print("O valor final é de:", vpreco)