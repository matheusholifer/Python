Um código simples para testar os operadores aritméticos em python.

```python
import math
import random as rd

try:
    n = (int(input("\nInsira um número inteiro: ")))

    a = rd.randrange(1, 10, 2) # Gera números pares no intervalo [1, 10]
    b = rd.randrange(1, 10, 3)  # Gera números impares no intervalo [1, 10]

    print("\nIniciando programa para testar Operadores Aritméticos...")

    print(f"\n\tA soma de {a} com {b} = {a + b}")

    c = rd.uniform(0.0, 10.0) # Gera um número de ponto flutuante no intervalo [0.0, 10.0]
    print(f"\n\tA subtração de {c} com {n} = {c - n:.2f}")

    print(f"\nO programa gerou {n} números: ")

    numeros = []
    contador = 1
    while contador < n:
        elemento = rd.randint(1, 100) # Gera números no intervalo [1, 100]
        numeros.append(elemento)
        contador += 1 # contador = contador + 1

    print(f"\n\t{numeros}")

    print(f"\tA Multiplicação = {math.prod(numeros)}") # Saída: A multiplicação de cada elemento da lista

    print(f"\n\tA divisão de {math.prod((numeros))} com {n} = {math.prod((numeros)) / n}")
    print(f"\n\tO resto da divisão de {math.prod((numeros))} com {n} = {math.prod((numeros)) % n}")

    print("\nO programa para testar Operadores Aritméticos finalizou com sucesso!\n")

except ValueError:
    print("\nVocê deve inserir um número inteiro!")
```
