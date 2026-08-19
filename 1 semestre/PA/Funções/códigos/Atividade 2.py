from funcoes import media_aproveitamento

nota, ma= 0.0, 0.0

while True:
        media=[]
        for i in range(1,4):
            nota= float(input(f"Coloque a nota {i}: "))
            if nota<0:
                  exit()
            media.append(nota)
        ma= media_aproveitamento(media[0], media[1], media[2])
        if ma>=9:
              print(f"O M.A desse aluno é {ma}, então seu conceito é A")
        elif ma>=7.5 and ma<9:
              print(f"O M.A desse aluno é {ma}, então seu conceito é B")
        elif ma>=6 and ma<7.5:
              print(f"O M.A desse aluno é {ma}, então seu conceito é C")
        elif ma>=4 and ma<6:
              print(f"O M.A desse aluno é {ma}, então seu conceito é D")
        else:
              print(f"O M.A desse aluno é {ma}, então seu conceito é E")