'''
    13) Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno.
    Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. Fórmula para o cálculo da média final é:

    mediafinal = (n1 * 2 + n2 * 3 + n3 * 5) / 10
'''

# Coleta de dados
nota1, nota2, nota3 = map(float, input("\nInsira as três notas do aluno, separadas por vírgula e espaço (Exemplo: 10, 6, 8): ").split(', '))

# Cálculo da média final
mediafinal = lambda n1, n2, n3: (n1 * 2 + n2 * 3 + n3 * 5) / 10

# Imprime relatório
print(f"\nA média final do aluno foi: {mediafinal(nota1, nota2, nota3):.2f} pontos")