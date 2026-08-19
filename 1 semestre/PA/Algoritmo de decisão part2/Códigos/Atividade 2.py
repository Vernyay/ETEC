vsalario, vtempo, vfilhos, vtempocasado, vhorasextras, vreajuste= 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

vsalario= float(input("Coloque seu salário atual:"))
vtempo= int(input("Coloque seu tempo de contribuição:"))
vfilhos= int(input("Coloque a quantidade de filhos que você tem:"))
vtempocasado= int(input("Coloque seu tempo de casado (em ano):"))
vhorasextras= int(input("Coloque a quatidade de horas extra que você fez no ultimo mês:"))

if vtempo>5 and vfilhos>2 and vtempocasado>2 and vhorasextras>10:
    vreajuste= vsalario*0.05
    print("Você vai receber o bônus no salário, seu novo salário será de:", vsalario+vreajuste, "Reais!!")

else:
    print("Você não atendeu a todos os requisitos, você vai continuar com o mesmo salário!!")