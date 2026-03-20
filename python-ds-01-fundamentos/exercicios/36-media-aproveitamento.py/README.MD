41) Faça um algoritmo para ler as 3 notas obtidas por um aluno nas 3 verificações e a média dos
exercícios que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula abaixo
e escrever o conceito do aluno de acordo com a tabela de conceitos mais abaixo:

media_de_aproveitamento = (N1 + N2 * 2 + N3 * 3 + Média_dos_Exercícios) / 7

A atribuição de conceitos obedece a tabela abaixo:

Média de Aproveitamento | Conceito
>= 9.0               A
>= 7.5 e < 9.0       B
>= 6.0 e < 7.5       C
< 6.0                D

```python
# Coleta de Dados
nota1, nota2, nota3 = map(float, input("\nEnter the student's three grades, separated by commas and spaces. (Ex: 10, 8, 9): ").split(', '))
media_dos_exercicios = float(input("\nEnter the average grade obtained by the student at the end of the exercises: "))

# Cálculo da Média de Aproveitamento
media_de_aproveitamento = (nota1 + nota2 * 3 + nota3 * 3 + media_dos_exercicios) / 7

# Atribuição de Conceito com base na Média Obtida
if media_de_aproveitamento >= 9.0:
    conceito = 'A'
elif media_de_aproveitamento >= 7.5 and media_de_aproveitamento < 9.0:
    conceito = 'B'
elif media_de_aproveitamento >= 6.0 and media_de_aproveitamento < 7.5:
    conceito = 'C'
else:
    conceito = 'D'

# Relatório
print(f"\nO conceito do aluno com Média de Aproveitamento igual a {media_de_aproveitamento:.2f} pontos, é = {conceito}.")s
```
