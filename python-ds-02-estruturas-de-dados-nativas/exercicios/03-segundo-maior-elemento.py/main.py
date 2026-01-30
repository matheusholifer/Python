'''
    4) Encontre o segundo maior elemento em uma lista de números.
'''

lista = [2, 1, 4, 5, 3, 11, 11]

# Remove duplicatas e ordena
lista_unica = sorted(set(lista))

if len(lista_unica) < 2:
    print("A lista não possui elementos suficientes.")
else:
    print(f"O segundo maior elemento é: {lista_unica[-2]}")