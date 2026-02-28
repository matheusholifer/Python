7. Intercale duas listas ordenadas em uma única lista também ordenada.

```python
# Definindo os Elementos das Listas
lista_quadrados = [x**2 for x in range(5)] # Resultado: 0, 1, 4, 9, 16
lista_pares = [x for x in range(10) if x % 2 == 0] # Resultado: 0, 2, 4, 6, 8

# Nova Lista Ordenada com os Elementos das Listas Anteriores
lista_final = sorted(lista_quadrados + lista_pares)

# Relatório Final
print(f"\nLista final = {lista_final}")
```
