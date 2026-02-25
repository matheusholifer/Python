22) A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais
de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%.
Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva
o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas
(considere que o mês possua 4 semanas exatas).

```python
# Coleta de Dados
while True:
    horas_trabalhadas = float(input("\nInsira quantas horas o funcionário trabalhou no mês: "))

    if horas_trabalhadas >= 200:
        break
    else:
        print("ERRO: Para este cálculo, insira um valor a partir de 200 horas")

salario_por_hora = float(input("\nInsira quanto o funcionário recebe por hora: R$"))

# Cálculo do Salario Total
# Para quem trabalha 40 horas semanais, o "divisor" padrão utilizado pela lesgilação brasileira é 200.
# (40 horas / 6 dias) x 30 dias do Mês = 200 horas/mês
extras = horas_trabalhadas - 200
salario_total = (200 * salario_por_hora) + (extras * (salario_por_hora + (salario_por_hora * 0.5)))

print(f"\nO salário total do funcionário é = R${salario_total}")
```
