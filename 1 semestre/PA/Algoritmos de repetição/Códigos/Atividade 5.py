import random

vnumerosecreto, vtentativas, vacertou, vchute= 0, 1, False, 0
vnumerosecreto=random.randint(1, 10)


while vtentativas <= 3:
    vchute = int(input(f"Tentativa {vtentativas}/3 - Digite seu palpite: "))

    if vchute == vnumerosecreto:
        print(f"Parabéns! Você descobriu o número {vnumerosecreto}!")
        vacertou = True
        break
    elif vchute < vnumerosecreto:
        print("Dica: O número secreto é MAIOR.")
    else:
        print("Dica: O número secreto é MENOR.")

    vtentativas += 1

if not vacertou:
    print("-" * 40)
    print(f"Que pena! Suas chances acabaram. O número era {vnumerosecreto}.")