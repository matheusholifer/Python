2) Inverta uma lista sem usar o método reverse().

```python
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
```

- Note que no código acima foi usado list comprehension, confira outros métodos abaixo:

### Fatiamento (Slicing)

```python
lista = [1, 2, 3, 4, 5]
invertida = lista[::-1] # [5, 4, 3, 2, 1]
```

### Função reversed()

```python
lista = [1, 2, 3, 4, 5]
invertida = list(reversed(lista)) # [5, 4, 3, 2, 1]
```

### Loop For - Inversão Manual

```python
lista = [1, 2, 3, 4, 5]
invertida = []
for i in range(len(lista)-1, -1, -1):
    invertida.append(lista[i]) # Cria uma nova lista invertida
```
                   
### Troca de Elementos (In-place - Sem alterar original)

```python
lista = [1, 2, 3, 4, 5]
n = len(lista)
for i in range(n // 2):
    # Troca elementos usando atribuição múltipla
    lista[i], lista[n - 1 - i] = lista[n - 1 - i], lista[i]

```
