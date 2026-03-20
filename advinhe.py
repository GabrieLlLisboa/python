

print("Bem vindo ao Jogo de Descobrir números.")
print("O computador escolheu um número de 1 a 10. Tente advinhar!")

# import 

import random

# variaveis

numero_secreto = random.randint(1, 10)
tentativa = 0
tentativas_contador = 0
limite = 5

# codigo

while tentativa != numero_secreto and tentativas_contador < limite:
    tentativa = int(input("Tente descobrir o número de 1 a 10: "))
    tentativas_contador += 1

    if tentativa < numero_secreto:
        print("número mais baixo do que o que eu escolhi")
    elif tentativa > numero_secreto:
        print("número é maior do que o que eu escolhi")
    else:
        print(f"acertou, voce precisou de {tentativas_contador} tentativas.  ")