vnum, vcont, vresultado= 0, 0, 0

vnum= int(input("Coloque um número:"))

for vcont in range(1,11):
    vresultado=vnum*vcont
    print(f"{vnum}X{vcont}={vresultado}")