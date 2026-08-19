vnota1, vnota2, vnota3, vnota4, vfaltas, vaulas, vmedia, vpresenca= 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

vnota1= float(input("Quanto você tirou na primeira prova:"))
vnota2= float(input("Quanto você tirou na segunda prova:"))
vnota3= float(input("Quanto você tirou na terceira prova:"))
vnota4= float(input("Quanto você tirou na quarta prova:"))
vmedia= (vnota1+vnota2+vnota3+vnota4)/4
vpresenca= ((((vaulas-vfaltas)*100)/vaulas))
vaulas= int(input("Quantas aulas teve:"))
vfaltas= int(input("Quantas aulas você faltou:"))

if ((((vaulas-vfaltas)*100)/vaulas))>=75:
    if vmedia>=7:
        print("Aluno Aprovado!!")
    elif vmedia>=5 and vmedia<7:
        print("Aluno de Recuperação!!!")
    else:
        print("Aluno Reprovado!!!")
else:
    print("Aluno reprovado por falta!!!")