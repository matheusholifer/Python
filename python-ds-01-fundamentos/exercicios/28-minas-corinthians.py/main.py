'''
    32) Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome
    do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.
'''

# Coleta de Dados
a = input("\nInsira o nome do primeiro time: ")
b = input("\nInsira o nome do segundo time: ")

ag = int(input("\nInsira o número de gols do primeiro time: "))
bg = int(input("\nInsira o número de gols do segundo time: "))

# Relátorio de Vitória ou Empate
if ag > bg:
    print(f"\nO {a} ganhou do {b}. Placar: {ag} x {bg}")
elif bg > ag:
    print(f"\nO {b} ganhou do {a}. Placar: {bg} x {ag}")
else:
    print(f"\nO {a} empatou com o {b}. Placar: {ag} x {bg}.")