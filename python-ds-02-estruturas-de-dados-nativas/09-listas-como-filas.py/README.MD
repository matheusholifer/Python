Um código introdutório ao uso de filas em Python.

```python
import random
from collections import deque

# criando uma fila vazia
fila = deque()

opcao = None

while opcao != 0:
    print("\n\tPress 0 to finish\n\tPress 1 to add an integer\n\tPress 2 to remove an integer\n\tPress 3 to view queue status")
    opcao = int(input("\n\t>>> "))

    match opcao:
        case 0:
            print("\nEnding the computer program...\n")

        case 1:
            numero = random.randint(1, 1000);
            fila.append(numero) # Adiciona x ao lado direito (final da fila).
            if numero in fila:
                print(f"\nThe number {numero} was successfully entered!")

        case 2:
                removido = fila.popleft() # Remove e retorna o elemento do lado esquerdo.
                print(f"\nThe number {removido} was successfully removed!")

        case 3:
            print(f"\nQueue data structure (size {len(fila)}): {fila}\n")

        case _: # Opção default
            print("\nInvalid option entered.\n")
```

- Note o uso de 'from collections import deque'. Se você usar uma lista comum do Python como fila (list.pop(0)), o Python precisa deslocar todos os outros elementos uma posição para a esquerda. Isso torna a operação lenta conforme a lista cresce:

Lista: Tempo de remoção é $O(n)$.

Deque: Tempo de inserção e remoção é $O(1)$ (constante), não importa o tamanho da fila.
