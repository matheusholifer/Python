Um código introdutório a List Comprehensions em Pythn.

```python
"""
    Compreensão de Listas (List Comprehensions)
    Forma concisa de criar listas. Útil para aplicar uma operação a cada elemento de uma sequência ou filtrar elementos.
"""

# Criando uma lista de quadrados sem compreensão de listas
quadrados = []
for x in range(10):
    quadrados.append(x**2)

print(f"{quadrados=}")

# Criando uma lista de quadrados com compreensão de listas
quadradoslc = [x**2 for x in range(10)]

print(f"{quadradoslc=}")

# Usando filtros (condicioanis)
pares_ao_quadrado = [x**2 for x in range(10) if x % 2 == 0] # Apenas quadrados de números pares

print(f"{pares_ao_quadrado=}")
```
