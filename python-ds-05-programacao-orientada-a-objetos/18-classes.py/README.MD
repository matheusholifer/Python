Um código introdutório a classes em Python.

```python
class Cachorro:
    # Atributo da classe (compartilhado por todas as instâncias)
    especie = 'mamífero'

    # Construtor
    def __init__(self, nome, idade):
        self.nome = nome # Atributo de instância
        self.idade = idade # Atributo de instância

    # Método para latir
    def latir(self):
        return f"{self.nome} está latindo!"

# Criando objetos (cachorros)
rex = Cachorro("Rex", 3)
toto = Cachorro("Totó", 5)

print(f"{rex.nome} tem {rex.idade} anos.") # Saída: Rex tem 3 anos.
print(toto.latir()) # Saída: Totó está latindo!
print(toto.especie) # Saída: mamífero
```
