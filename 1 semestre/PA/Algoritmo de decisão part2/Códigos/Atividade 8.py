vcodigo, vdescricao= 0.0, ""

vcodigo= int(input("Coloque o código do produto:"))
vdescricao= ["Alimento não-perecível", "Alimento perecível", "Vestuário", "Higiene pessoal", "Utensílios domésticos"]

if vcodigo==1:
    vdescricao=vdescricao[0]
elif vcodigo==2 or vcodigo==3 or vcodigo==4:
    vdescricao=vdescricao[1]
elif vcodigo==5 or vcodigo==6:
    vdescricao=vdescricao[2]
elif vcodigo==7:
    vdescricao=vdescricao[3]
elif vcodigo==8 or vcodigo==9 or vcodigo==10:
    vdescricao=vdescricao[4]

if vcodigo<=10:
    print("Esse item é um:", vdescricao)
else:
    print("Produto inválido")