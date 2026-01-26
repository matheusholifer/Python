'''
    10) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do
    distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor
    seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro,
    calcular e escrever o custo final ao consumidor.
'''

# coleta de dados
custo_de_fabrica = float(input("\nInsira o custo de fábrica do carro: "))

# Cálculo do custo final ao consumidor
porcentagem_distribuidor = (28/100) * custo_de_fabrica
impostos = (45/100) * custo_de_fabrica

custo_final = lambda c, p, i: c + p + i

print(f"\n\tO custo final ao consumidor é: R${custo_final(custo_de_fabrica, porcentagem_distribuidor, impostos):.2f}")