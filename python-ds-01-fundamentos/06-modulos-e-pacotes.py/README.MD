Um código simples, exemolificando a criação de minhas próprias bibliotecas em python.

### mylib.py

```python
def saudacoes(nome):
    return f"Olá, {nome}! Bem vindo a minha biblioteca Python."
```

### main.py

```python
import mylib

nome = "Matheus"

print(mylib.saudacoes(nome))
```
