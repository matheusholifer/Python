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
