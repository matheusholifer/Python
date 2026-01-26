'''
    9) Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
    Calcular e escrever o valor do novo salário.
'''

# Coleta dos dados
salario_atual = float(input("\nInsira o salário atual do funcionário: "))
porcentual_reajuste = int(input("\nInsira o porcentual do reajuste (int): "))

# Cálculo do novo salário
aumento = (porcentual_reajuste / 100) * salario_atual
salario_final = salario_atual + aumento

# Relatório
print(f"\n\tO novo salário deve ser de R${salario_final}")