4) Encontre o segundo maior elemento em uma lista de números.

### Usando método sorted

```python
lista = [2, 1, 4, 5, 3, 11, 11]

# Remove duplicatas e ordena
lista_unica = sorted(set(lista))

if len(lista_unica) < 2:
    print("A lista não possui elementos suficientes.")
else:
    print(f"O segundo maior elemento é: {lista_unica[-2]}")
```

### Usando laço for manual
```python
# Cria uma lista númerica
lista = [1, 2, 3, 4, 5, 6, 7, 8]

# Variável para armazenar o maior elemento
maior = 0

# Loop for para percorrer a lista e encontrar o maior elemento
for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]

print(f"\nO maior elemento da lista é = {maior}.")

# Remove o atual maior elemnto da lista
lista.remove(maior)

# Variável para armazenar o segundo maior elemento
segundo_maior = 0

# Loop para percorrer a lista e encontrar o segundo maior elemento (atual maior elemnto da lista
for i in range(len(lista)):
    if lista[i] > segundo_maior:
        segundo_maior = lista[i]

print(f"\nO segundo maior elemento da lista é = {segundo_maior}.")
```

### Usando método sort (altera a ordem original)

```python
# Cria uma lista númerica
lista = [2, 1, 4, 5, 3, 11]

# Ordena os elemntos da lista
lista.sort()

print(f"\nO segundo maior elemnto da lista é = {lista[len(lista) - 2]}")
```
