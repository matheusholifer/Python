'''
    16) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
    compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
    escreva o custo total da compra
'''

# Entrada de dados
quantidade = int(input("Insira quantas maçãs foram compradas: "))

# A lambda agora usa o parâmetro 'n' corretamente para o cálculo
calcular_custo = lambda n: n * 1.30 if n < 12 else n * 1.00

# Execução e formatação
total = calcular_custo(quantidade)
print(f"O custo total da compra é: R$ {total:.2f}")