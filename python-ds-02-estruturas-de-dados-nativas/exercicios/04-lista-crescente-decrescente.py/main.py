'''
    5. Verifique se uma lista está ordenada de forma crescente.
'''

# Criação das listas
lista1 = [1, 2, 3, 4, 5, 6, 7, 8] # Lista crescente
lista2 = [8, 7, 6, 5, 4, 3, 2, 1] # Lista decrescente

# Em progressões aritméticas P.As, você pode achar o valor da razão
# pela seguinte fórmula expandida r = ak - ap / k - p
# tal que ak: O valor do termo que está na frente
#         ap: O valor do termo que está atrás
#         k e p: As posições desses termos
r = (lista1[1] - lista1[0]) / 1 - 0

# Condição para ser crescente
# O termo anterior será menor que o próximo se (an-1 < an) se,
# e somente se a razão for positiva
if r > 0:
    print(f"\nA {lista1=} está ordenada de forma crescente. ")
else:
    print(f"\nA {lista1=} está ordenada de forma decrescente. ")

# Teste com a lista decrescente
r2 =  (lista2[1] - lista2[0]) / 1 - 0
status_lista = lambda r: "Lista Crescente" if r > 0 else "Lista Descrescente"

# relatório para a Lista Decrescente
print(status_lista(r2))