Um código introdutório a herança multípla em Python.

```python
# Exemplo prático de Herança Multipla em Python
class AnimalTerrestre:
    def andar(self):
        print("\nAndando em terra...")

class AnimalAquatico:
    def nadar(self):
        print("\nNadando em água...")

# A classe Anfíbio herda de ambas
class Anfibio(AnimalTerrestre, AnimalAquatico):
    pass

# Instanciando a classe que herda de ambas
agente = Anfibio()
agente.nadar()
agente.andar()
```
