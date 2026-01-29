''''
    2) Inverta uma lista sem usar o método reverse().
'''

# Cria uma lista com elementos de 'A' a 'D'
lista = ['A', 'B', 'C', 'D']

# Imprime a lista antes da inversão
print(f"{lista=}")

'''
    Inverte usando list comprehension e range com passo negativo

    len(lista): Retorna o número de elementos
    range(start, stop, step):
    
        start (len(lista) - 1): Listas em python começam no índice 0, logo, o último elemento de uma lista de 4 elementos está no índice 3
        stop (-1): Ele para um índice antes, então ele para no índice 0
        step (-1): Indica que a contagem deve ser decrescente   
'''
lista_invertida = [lista[i] for i in range(len(lista) -1, -1, -1)]

# Imprime a lista após a inversão
print(f"{lista_invertida=}")

