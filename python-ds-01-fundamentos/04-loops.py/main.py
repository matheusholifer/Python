# Listas pré-preenchidas
personagens_marvel = ["Captain America", "Iron Man", "Thor", "Quicksilver"]
personagens_dc = ["Superman", "Batman", "Flash", "Green Lantern"]

# Exemplos com loop for
print("\nPersonagens da Marvel:")
for personagem in personagens_marvel:
    print(f"\n\t{personagem}")

print("\nPersonagens da DC:")
for personagem in personagens_dc:
    print(f"\n\t{personagem}")

print("\nNúmeros inteiros de 0 a 100:")
print("\t", end=" ")
for i in range(100):
    print(i, end=" ") # O Parâmetro end=" " serviu para mostrar a sequência lado a lado, com um 'espaço' entre os números

print("\n\nNúmeros pares de 0 a 100: ")
print("\t", end=" ")
for i in range(0, 102, 2):
    print(i, end=" ")

print("\n\nNúmeros impares de 0 a 100: ")
print("\t", end=" ")
for i in range(1, 100, 2):
    print(i, end=" ")

# Exemplos com loop while

print("\n")
contador = 1
while contador <= 3:
    print(f"\nContagem: {contador}°")
    contador+=1

# Uma lista e un indice para percorrer com loop while
lista_velocistas = ["Barry Allen", "Pietro Maximoff", "Carin Taylor"]
indice = 0

print("\n")
while indice < len(lista_velocistas):
    print(lista_velocistas[indice])
    indice+=1


