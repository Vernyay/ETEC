def soma(vn1,vn2):
    soma=vn1+vn2
    return soma

def media_aproveitamento(vn1,vn2,vn3):
    MA= (vn1+vn2*2+vn3*3)/6
    return MA

def maior_num(lista):
    maior= lista[0]
    for i in lista[1:]:
        if i>maior:
            maior=i
    return maior

def taxa(int):
    if int==1:
        aplica = -5.0  # %
    elif int==2:
        aplica = 1.0  # %
    elif int==3:
        aplica = 4.5  # %
    elif int==4:
        aplica = 7.5  # %
    else:
        aplica = 10.0  # %
    return aplica

def calculo_percentual(qtd, percentual):
    valor = (qtd * percentual) / 100
    return valor

def nota(nt1, nt2, nt3, nt_tipo):
    if nt_tipo == "A":
        media= (nt1+nt2+nt3)/3
    else:
        media= ((nt1*5)+(nt2*3)+(nt3*2))/ 10
    return media

def categoria(idade):
    if idade>=5 and idade<=7:
        return "Infantil A"
    elif idade>=8 and idade<=10:
        return "Infantil B"
    elif idade>=11 and idade<=13:
        return "Juvenil A"
    elif idade>=14 and idade<=17:
        return "Juvenil B"
    else:
        return "Adulto"
    
def positivo(valor):
    if valor >= 0:
        return True
    return False

def par(int):
    if int%2==0:
        return True
    else:
        return False

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def reajuste_salario(salario, filhos):
    if salario[0] < 1000:
        percentual = 9
    elif salario[0] <= 3000:
        percentual = 7
    else:
        percentual = 5

    if filhos < 3:
        percentual += 1
    else:
        percentual += 2

    salario[0] = salario[0] + (salario[0] * percentual / 100)
    return percentual