3) Remova todos os elementos duplicados de uma lista.

```python
print("\nPrograma para remoção dos elemntos de uma lista:")

# Cria uma lista com elementos repetidos
lista_unica = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8]

print(f"\n\t{lista_unica=}")

# Cria uma lista vazia
lista_comprimida = []

# Copia os elementos únicos da lista original para a lista comprimida
[lista_comprimida.append(elemento) for elemento in lista_unica if elemento not in lista_comprimida]

print(f"\n\t{lista_comprimida=}")
```
