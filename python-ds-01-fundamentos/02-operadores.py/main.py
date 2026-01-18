import random

hp_personagem = 100
forca_personagem = 100

hp_criatura = 300
forca_criatura = 150

print("\n'Matheus, o Bardo', utilizou sua flauta mágica para conjurar a 'Espada de Ares'!")

# 1. Multiplicação e Uniform (Sorteio do modificador)
modificador = random.uniform(0.5, 2.0)
dano_calculado = forca_personagem * modificador

# 2. Divisão (Apenas para exibir uma estatística de poder, por exemplo)
poder_relativo = hp_criatura / forca_personagem

print(f"\tO dano potencial é de {dano_calculado:.2f} (Modificador: {modificador:.2f}x)")
print(f"\tA criatura tem {poder_relativo:.1f}x mais vida que sua força.")

chance_de_acerto = random.randint(0, 100)

# 3. Adição (Bônus de sorte se o número for par, usando Resto da Divisão %)
if chance_de_acerto % 2 == 0:
    dano_calculado += 10  # Bônus de precisão
    print("\tBônus de sorte aplicado! +10 de dano.")

if chance_de_acerto > 30:  # 70% de chance de acerto
    print("\n\t'Matheus, o Bardo' acertou o 'Minotauro de Três Cabeças'!")

    # 4. Subtração
    hp_criatura -= dano_calculado

    if hp_criatura <= 0:
        print(f"\n\t\tO minotauro recebeu {dano_calculado:.2f} de dano e sangra ao chão.\n")
        print("\t\tVocê venceu!\n")
    else:
        print(f"\n\t\tO Minotauro sobreviveu (HP: {hp_criatura:.2f}) e contra-ataca!\n")

        # Contra-ataque
        hp_personagem -= forca_criatura
        print(f"\tVida atual do herói: {hp_personagem}")

        if hp_personagem <= 0:
            print('\n\tVocê morreu!')
else:
    print("\n\tVocê errou o ataque e o Minotauro ri da sua cara!")