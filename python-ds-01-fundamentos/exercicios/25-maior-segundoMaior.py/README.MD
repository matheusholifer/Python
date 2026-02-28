29) Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

```python
# Coleta de Dados
a, b, c = map(float, input("\nInsira 3 valores quaisquer, separados por vírgula e espaço: ").split(', '))

# Encontrando o Maior e o Segundo Maior valor
m1 = max(a, max(b, c))
m2 = (a + b + c) - m1 - min(a, min(b, c))

# Relátório Final
print(f"\nA soma de {m1} com {m2} = {m1 + m2}")
```
