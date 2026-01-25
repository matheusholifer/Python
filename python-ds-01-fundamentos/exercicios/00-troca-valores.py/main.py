'''
    1) Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B.
    A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o
    valor que está em A passe para B e vice-versa. Ao final, escrever os valores que ficaram armazenados
    nas variáveis.
'''

a = 10
b = 20

print(f"\nVáriavel {a=} e váriavel {b=} antes da troca...")

# Usando varíavel auxiliar
aux = a
a = b
b = aux

# Usando operações básicas
a = a + b # A agora é 30
b = a - b # B agora é 10
a = a - b # A agora é 20

# Usando operador bit a bit
a = a ^ b
b = a ^ b
a = a ^ b

print(f"\nVáriavel {a=} e váriavel {b=} depois da troca.")
print("\nPrograma finalizou com sucesso!")