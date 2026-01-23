Um código que exemplifica o uso de tuplas em python.

```python
"""
    Tuplas e sequências
    Tuplas são sequências imutáveis. Elas são definidas por parênteses () e vírgulas
"""

# Parênteses são opicionais, mas são uma boa prática
herois = ("Captain America", "Flash", "Quicksilver", "Guardian")

sentinela_da_liberdade, velocista_escarlate, nao_identificado, clone_cadmus23423 = herois

# O Python conta a partir do zero
print(f"{herois[0]}:{sentinela_da_liberdade}")

print(f"{sentinela_da_liberdade=}") # Saída: sentinela_da_liberdade='Captain America'

print(f"{herois[1]=}") # Saída: herois[1]='Flash'

print(f"{herois[2]}") # Saída: Quicksilver

# Tuplas em Python são imutáveis, logo, tentar alterar um valor (ex: herois[3] = "Green Lantern") gera um TypeError
try:
    herois[3] = "Green Lantern"
except TypeError:
    print("Erro: Tuplas são imutáveis e não podem ser alteradas.")

# Coordenadas aproximadas da sede da Warner Bros. Studios, 34.1507° N, 118.3340° W
coordenadas = 34.1507, 118.3340

print(f"{coordenadas[0]}° N - {coordenadas[1]}° W")

# Criando tuplas vazias
defeitos_serie_Peacemaker = ()

# Criando tuplas com um item
melhores_atores_spiderman = ('Tobey Maguire',) # Obrigatório uso de vírgula
```

- Tuplas são sequências imutáveis.
