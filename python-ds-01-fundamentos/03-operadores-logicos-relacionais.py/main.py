import random

numero = random.randint(1, 10)

chute = 0
while chute != numero: # Diferente de
    chute = int(input("\nInsira um número no intervalo [1, 10]: "))

    if chute < 1 or chute > 10:
        print("\tAVISO: Você chutou fora do intervalo de 1 a 10!")

    if chute < numero: # Menor que
        print(f"\n\tTente um número maior que {chute}.")
    elif chute > numero: # Maior que
        print(f"\n\tTente um número menor que {chute}.")
    else:
        print("\n\tVocê acertou!")
