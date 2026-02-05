Um código introdutório a heranças em Python.

```python
# Exemplo Prático de Herança em Python
class Animal: # Classe pai (Base)
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass # Método a ser sobrescrito

class Cachorro(Animal): # Classe filha (derivada)
    def emitir_som(self):
        return f"{self.nome} diz: Au Au!"

meu_cao = Cachorro("Totó")
print(meu_cao.emitir_som()) # Saída: Totó diz: Au Au!
```
