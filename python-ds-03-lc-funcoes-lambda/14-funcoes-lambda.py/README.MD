Um código introdutório de Funções Lambda em Python.

```python
"""
    Funções Lambda (lambda argumentos: expressão)
    São funções anônimas (sem nome), pequenas e de uso único.
"""

# Função que multiplica um elemento x por 2
def dobrar(x):
    return x * 2

print(f"{dobrar(10)=}") # Saída: dobrar(10)=20

# Função anônima que multiplica um elemento x por 2
dobrarlbd = lambda x: x * 2

print(f"{dobrarlbd(5)=}") # saída: dobrarlbd(5)=10
```
