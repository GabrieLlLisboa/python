# import 

import random

# variaveis

numero_secreto = random.randint(1, 10)
tentativa = 0

# codigo

while tentativa != numero_secreto:
    tentativa = int(input("Tente descobrir o número de 1 a 10."))

    if tentativa < numero_secreto:
        print("número mais baixo do que o que eu escolhi")
    elif tentativa > numero_secreto:
        print("número é maior do que o que eu escolhi")
    else:
        print("acertou")