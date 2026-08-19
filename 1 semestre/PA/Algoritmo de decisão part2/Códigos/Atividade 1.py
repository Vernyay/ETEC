vsalario, vreajuste, vsexo= 0.0, 0.0, 0

vsalario= float(input("Coloque seu salário atual:"))
vsexo= int(input("Coloque seu sexo, sendo 1 para Feminino e 2 para masculino:"))

if vsexo==1 and vsalario<2000:
    vreajuste= vsalario*0.02
elif vsexo==1 and vsalario>=2000:
    vreajuste= vsalario*0.05
elif vsexo==2 and vsalario<2500:
    vreajuste= vsalario*0.04
else:
    vreajuste= vsalario*0.07

print("Seu salário reajustado será de:", vsalario+vreajuste, "Reais!!")