Um código que exemplifica o uso de dicionários em Python.

```python
"""
    Dicionários (Dictionaries)
    São mapas de chaves para valores. As chaves devem ser tipos imutáveis (como strings, números ou tuplas que só contenham objetos imutáveis).
"""

import time # Para formatação de datas e horas

# Criando um dicionário diretamente
atividades = {'xadrez': 10.0, 'inglês': 10.4, 'leitura': 11.0, 'estudar': 13.0, 'academia': 15.0}

print(f"{atividades=}")

# Criando um dicionário com o construtor dict()
temas = dict(python='Dicionários', sql='Select')

print(f"{temas=}")

# Criando um dicionário vazio
ferramentas = {}

# Fazendo inserções no dicionário vazio
ferramentas['Pycharm'] = 'Python'
ferramentas['pgAdmin4'] = 'PostgreSQL'

print(f"{ferramentas=}")

# Removendo item de um dicionário
del temas['sql'] # ou temas.pop('sql')

print(f"{temas=}")

# Iterando sobre dicionários
for chave in ferramentas.keys():
    print(chave)

for valor in ferramentas.values():
    print(valor)

for chave, valor in ferramentas.items():
    print(f"{chave}:{valor}")

```
