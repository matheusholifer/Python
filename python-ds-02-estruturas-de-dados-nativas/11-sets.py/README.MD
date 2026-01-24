Um código que exemplifica o uso de sets em python.

```python
"""
    Conjuntos (Sets)
    Um conjunto é uma coleção não ordenada e sem elementos duplicados. Útil para testar pertinência e eliminar duplicatas.
"""

# Criando um conjunto
filmes = {"2001: A Space Odyssey", "Apollo 11", "Cosmos: A Spacetime Odyssey", "Interstellar", "Cosmos: A Spacetime Odyssey"} # Os conjuntos removem duplicatas automaticamente

# Criando um conjunto vazio
series = set()

print(f"\nFilmes: {filmes}") # Filmes: {'Apollo 11', '2001: A Space Odyssey', 'Cosmos: A Spacetime Odyssey', 'Interstellar'}

# Adicionando elementos
filmes.add("Gravity")
filmes.update(["Interstellar", "How the Universe Works"])

print(f"\nFilmes: {filmes}") # Filmes: {'Apollo 11', 'Gravity', 'Cosmos: A Spacetime Odyssey', 'Interstellar', '2001: A Space Odyssey', 'How the Universe Works'}

# Removendo elementos
filmes.remove("Cosmos: A Spacetime Odyssey") # Gera erro se o elemento não existir
filmes.discard("Superman(2025)") # Não gera erro se o elemento não existir)

print(f"\nFilmes: {filmes}") # Filmes: {'Apollo 11', 'Gravity', 'Interstellar', '2001: A Space Odyssey', 'How the Universe Works'}

# Operações com conjuntos
# União
A = {1, 2, 3}; B = {3, 4, 5}
print(f"\nConjunto A: {A}\nConjunto B: {B}\n\n\tConjunto união: {A|B} ") # | ou .union(): Junta dois conjuntos, removendo repetidos

print(f"\n\tConjunto intersecção: {A&B}") # & ou .intersection(): # Apenas elementos presentes em ambos

print(f"\n\tConjunto diferença: {A-B}") # - ou .difference(): Elementos apenas no conjunto da esquerda

print(f"\n\tConjunto simetria: {A^B}") # ^ ou .symmetric_difference(): Elementos em A ou B, mas não em ambos

# Verificando pertencimento

if "Gravity" in filmes:
    print("\nVerdade")
else:
    print("\nMentira")

```
