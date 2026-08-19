vnum, vcont, vresultado= 0, 0, 0

vnum= int(input("Coloque um número:"))

while vcont<=10:
    vresultado=vnum*vcont
    print(f"{vnum}X{vcont}={vresultado}")
    vcont+=1