'''
    17) Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever
    uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o
    aluno é aprovado). Escrever também a média calculada.
'''

# Coleta de dados
primeira_avaliacao, segunda_avaliacao = map(float, input("\nInsira as notas da primeira e segunda avaliação, separadas por vírgula e espaço: ").split(', '))

# Cálculo da Média Aritmética
resultado_final = lambda a, b: "Aprovado" if ((a + b) / 2) >= 6 else "Reprovado"

# Relatório
print(f"\nO aluno está {resultado_final(primeira_avaliacao, segunda_avaliacao)}!!!")