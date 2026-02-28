28) Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

```python
# Coleta de Dados
a, b, c = map(float, input("\nInsira 3 valores quaisquer, separados por vírgula e espaço: ").split(', '))

# Encontrando o Maior Valor
maior_valor = max(a, b, c)

# Relatório Final
print(f"\nO maior valor dentre {a}, {b}, {c} é = {maior_valor}")
```
