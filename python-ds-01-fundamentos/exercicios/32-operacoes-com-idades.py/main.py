'''
    36) Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades
    dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma
    das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais
    novo com a mulher mais velha.
'''

# Coleta de Dados
h1, h2 = map(int, input("\nInsira a idade dos dois homens, separadas por ', ': ").split(', '))
m1, m2 = map(int, input("\nInsira a idade das duas mulheres, separadas por ', ': ").split(', '))

# Criando Listas com as Idades
idade_homens = [h1, h2]
idade_mulheres = [m1, m2]

# Separando os Pares
homem_mais_velho = max(idade_homens)
mulher_mais_velha = max(idade_mulheres)

homem_mais_novo = min(idade_homens)
mulher_mais_nova = min(idade_mulheres)

# Relatório Final
print(f"\nA soma das idades do {homem_mais_velho=}, com a {mulher_mais_nova=} é igual a {homem_mais_velho + mulher_mais_nova}.")
print(f"\nO produto das idades do {homem_mais_novo}, com a {mulher_mais_velha} é igual a {homem_mais_novo * mulher_mais_velha}.")