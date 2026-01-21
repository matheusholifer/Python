Um código que apresenta a estrutura de funções em python.

- Fatorial de um número (Recursão)

```python

'''
    Função que cálcula o fatorial de um número recursivamente
'''
def fatorial_recursivo(n):
    # Caso base: Fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1

    # Passo recursivo: n! = n * (n - 1)!
    else:
        return n * fatorial_recursivo(n - 1)
```
