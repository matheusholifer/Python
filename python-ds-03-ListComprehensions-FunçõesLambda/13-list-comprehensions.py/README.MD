Um código introdutório as compreensão de listas em Python.

```python
"""
    Compreensão de Listas (List Comprehensions)
    Forma concisa de criar listas. Útil para aplicar uma operação a cada elemento de uma sequência ou filtrar elementos.
"""

# Criando uma lista de quadrados
quadrados = [x**2 for x in range(10)]

print(f"{quadrados=}") # Saída: quadrados=[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Com condiçaõ
pares = [x for x in range(10) if x % 2 == 0]

print(f"{pares=}") # Saída: pares=[0, 2, 4, 6, 8]
```
