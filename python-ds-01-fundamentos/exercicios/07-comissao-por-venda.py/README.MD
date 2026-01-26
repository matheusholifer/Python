11) Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
    mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele
    efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas
    vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do
    vendedor.

```python
# Coleta de dados
numero_carros_vendidos = int(input("\nInsira o número de carros vendidos: "))
valor_total_vendas = float(input("\nInsira o valor total das vendas: R$"))
salario_fixo = float(input("\nInsira o salário fixo: R$"))
valor_por_carro_vendido = float(input("\nInsira quanto o funcionário recebe por carro vendido: R$"))

# Cálculo do salario final
salario_final = lambda numero_carros, total_vendas, salario, valor_venda: (salario + (numero_carros * valor_venda) + ((5 / 100) * total_vendas))

# Relatório
print(f"\n\tO salário final do funcionário é R${salario_final(numero_carros_vendidos, valor_total_vendas, salario_fixo, valor_por_carro_vendido):.2f}")
```
