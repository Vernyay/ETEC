vdia, vsemana=0.0, ""

vdia= int(input("Coloque um número de 1 à 7:"))
vsemana= ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

if vdia==1:
    print("Esse número corresponde ao dia: ", vsemana[0])
elif vdia==2:
    print("Esse número corresponde ao dia: ", vsemana[1])
elif vdia==3:
    print("Esse número corresponde ao dia: ", vsemana[2])
elif vdia==4:
    print("Esse número corresponde ao dia: ", vsemana[3])
elif vdia==5:
    print("Esse número corresponde ao dia: ", vsemana[4])
elif vdia==6:
    print("Esse número corresponde ao dia: ", vsemana[5])
elif vdia==7:
    print("Esse número corresponde ao dia: ", vsemana[6])
else:
    print("Valor Inválido!!")