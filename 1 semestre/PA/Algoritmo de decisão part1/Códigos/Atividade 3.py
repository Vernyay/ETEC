vsalario, vnovosalario, vreajuste=0.0, 0.0, 0.0

vsalario= int(input("Coloque seu salário:"))

if vsalario<2000:
    vreajuste= 0.15
    vnovosalario=vsalario+(vsalario*vreajuste)
    print("Seu reajuste será de:", vsalario*vreajuste, "Reais")
    print("Seu novo sálario será:", vnovosalario, "Reais")

elif 2000<=vsalario<=5000:
    vreajuste= 0.10
    vnovosalario=vsalario+(vsalario*vreajuste)
    print("Seu reajuste será de:", vsalario*vreajuste, "Reais")
    print("Seu novo sálario será:", vnovosalario, "Reais")

else:
    vreajuste= 0.05
    vnovosalario=vsalario+(vsalario*vreajuste)
    print("Seu reajuste será de:", vsalario*vreajuste, "Reais")
    print("Seu novo sálario será:", vnovosalario, "Reais")