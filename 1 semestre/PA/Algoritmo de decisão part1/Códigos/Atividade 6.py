vidade, vcontribuicao= 0.0, 0.0
vidade= int(input("Informe sua idade:"))
vcontribuicao= int(input("Coloque seus anos de contribuição:"))

if vidade>=65:
    print("Aposentado")
elif vidade>=60 and vcontribuicao>=25:
    print("Aposentado")
elif vcontribuicao>=30:
    print("Aposentado")
else:
    print("Não está aposentado")