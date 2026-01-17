# Tipos string
nome_personagem = input("Nome do personagem: ")
classe_personagem = input("Classe do personagem: ")
raca_personagem = input("Raça do personagem: ")

# Tipos int (integer)
pontos_de_vida = int(input("\nHP: "))
pontos_de_forca = int(input("Força: "))
pontos_de_agilidade = int(input("Agilidade: "))

# Tipos float
peso_itens = float(input("\nPeso dos itens: "))
modificadores_de_dano = float(input("Modificadores de Dano: "))

# Tipo bool
esta_vivo = bool(input("\nEstá vivo: "))
possui_magia = bool(input("Possui magia: "))

# Tipos list
itens_player = input("Itens: ")
lista_itens = itens_player.split(',')

print("----------------------------------------------")

print(f"\n\tNome: " + nome_personagem);
print("\n\tClasse: " + classe_personagem);
print("\n\tRaça: " + raca_personagem);

print("\n\t\tHP: " + str(pontos_de_vida));
print("\n\t\tForça: " + str(pontos_de_forca));
print("\n\t\tAgilidade: " + str(pontos_de_agilidade));

print("\n\t\tMochila: " + str(peso_itens) + "KG");
print("\n\t\tModificadores de dano: " + str(modificadores_de_dano) + "x");

print(f"\n\tEstá vivo: {'Sim' if esta_vivo else 'Não'}");
print(f"\n\tPossúi mágia: {'Sim' if possui_magia else 'Não'}");

print(f"\n\tItens: {lista_itens}")

print("----------------------------------------------")