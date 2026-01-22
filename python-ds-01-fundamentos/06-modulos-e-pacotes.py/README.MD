Um código simples, exemolificando a criação de minhas próprias bibliotecas em python.

### mylib.py

```python
def saudacoes(nome):
    return f"Olá, {nome}! Bem vindo a minha biblioteca Python."
```

- Note que dentro do arquivo mylib.py, criamos uma função saudacoes.

### main.py

```python
import mylib

nome = "Matheus"

print(mylib.saudacoes(nome))
```

- No nosso main.py, importamos mylib e usamos a função declarada anteriormente.
