vsalario, vtempo, vreajuste= 0.0, 0.0, 0.0

vsalario= float(input("Coloque seu salário atual:"))
vtempo= int(input("Coloque seus anos de contribuição:"))

if vsalario>3000 and vtempo>5:
    vreajuste= vsalario*0.09
elif vsalario<3000 and vtempo>5:
    vreajuste= vsalario*0.12
else:
    vreajuste= vsalario*0.1

print("Seu reajuste vai ser de:", vreajuste)
print("Seu novo salário vai ser de:", vsalario+vreajuste)