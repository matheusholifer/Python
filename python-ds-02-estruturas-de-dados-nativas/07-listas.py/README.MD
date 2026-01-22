Um código introdutório ao estudo de estruturas de dados em python.

### main.py

```python
import random

lista = [] # lista = list()

opcao = None # Cria uma váriavel sem valor

while opcao != 0:
    print("\n\tPress 0 to finish\n\tPress 1 to add an integer\n\tPress 2 to remove an integer\n\tPress 3 to view list status")
    opcao = int(input("\n\t>>> "))

    match opcao:
        case 0:
            print("\nEnding the computer program...\n")

        case 1:
            numero = random.randint(1, 1000);
            lista.append(numero) # Adiciona um item ao fim da lista
            if numero in lista:
                print(f"\nThe number {numero} was successfully entered!")

        case 2:
            removido = int(input("\nEnter the value you want to remove: "))
            if removido in lista:
                lista.remove(removido) # Remove o primeiro item cujo valor seja igual a x
                print(f"\nThe number {removido} was successfully removed!")
            else:
                print(f"The number {removido} is not on the list.")

        case 3:
            print(f"\nList data structure (size {len(lista)}): {lista}\n")

        case _: # Opção default
            print("\nInvalid option entered.\n")
```

- Note o uso append (Adiciona um item ao fim da lista) e remove (Remove o primeiro item cujo valor seja igual a x)

### insert(i, x)

```python
case 4:
            numero = random.randint(1, 1000);
            posicao = int(input("\nEnter the position where you want to insert an element: "))
            lista.insert(posicao, numero) # Insere um item em uma posição dada.
            print(f"\nThe number {numero} was successfully entered!")
```

### clear()

```python
case 5:
            lista.clear()  # Remove todos os itens da lista.
            if len(lista) == 0:
                print("\nAll items in the list were successfully removed.")
```

### index(x)

```python
case 6:
            numero = int(input("\nEnter the key of the element you wish to query: "))
            if numero in lista:
                print(f"\nThe index of the number {numero} is {lista.index(numero)}") # Retorna o índice do primeiro item com valor x
```


### count(x)

```python
case 7:
            numero = int(input("\nEnter the key of the element you wish to query: "))
            if numero in lista:
                print(f"The number {numero} appears {lista.count(numero)} time(s)") # Retorna o número de vezes que x aparece.
```

### sort()

```python
case 8:
            lista.sort() # Ordena os itens da lista in place (na própria lista).
            print("List sorted successfully!")
```

### reverse()

```python
case 9:
            lista.reverse() # Inverte a ordem dos elementos.
            print("List elements successfully reversed!")
```

Outros métodos internos do Python não comentados:

1. lista.extend(iterable): Adiciona todos os itens de um iterável (outra lista, tupla, etc.) ao fim da lista.

2. list.copy(): Retorna uma cópia rasa da lista.

3. list.pop([i]): Remove e retorna o item na posição dada. Se nenhum índice for especificado, remove o último.
- O método pop() será comentado quando estudar pilhas











