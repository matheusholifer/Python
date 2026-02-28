'''
    6. Implemente uma função que rotacione uma lista à direita em k passos.
'''

# Definindo os Elementos da Lista
numeros = range(1, 6)
lista = [x**2 for x in numeros] # Resultado: [1, 4, 9, 16, 25]

# Imprimindo a Lista antes de Rotacionar
print(f"{lista=}")

# Definindo o Número de Passos
k = int(input("\nInsira o número de passos em que a lista será rotacionada: "))

# Rotacionando a Lista
lista_rotacionada = lista[-k:] + lista[:-k]

# Imprimindo a Lista depois de Rotacionar
print(f"\n{lista_rotacionada=}")