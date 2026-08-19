vnota1, vnota2, vmedia, vletra= 0.0,0.0,0.0,""

vnota1= float(input("Coloque a nota da primeira prova:"))
vnota2= float(input("Coloque a nota da segunda prova:"))
vmedia= (vnota2+vnota1)/2
vletra= ["A", "B", "C", "D", "E"]

if vmedia>=9.0 and vmedia<=10.0:
    vletra=vletra[0]
elif vmedia>=7.5 and vmedia<9.0:
    vletra=vletra[1]
elif vmedia>=6.0 and vmedia<7.5:
    vletra=vletra[2]
elif vmedia>4.0 and vmedia<6.0:
    vletra=vletra[3]
else:
    vletra= vletra[4]

print("Sua média é de:", vmedia)
print("Seu conceito é de:", vletra)

if vletra==vletra[0] or vletra==vletra[1] or vletra==vletra[2]:
    print("Aprovado!!")
else:
    print("Reprovado!!")