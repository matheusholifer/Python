Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que
ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que
ultrapassar este valor, calcular e escrever o seu salário total.

```python
# Coleta de Dados
salario_fixo = float(input("\nInsira o salário fixo do vendedor: "))
vendas_efetuadas = float(input("\nInsira o valor das vendas efetuadas pelo vendedor: "))

# Cálculo do Salário Final
comissao = (vendas_efetuadas * 0.03) if vendas_efetuadas <= 1500 else (45 + (vendas_efetuadas - 1500) * 0.05)
salario_final = salario_fixo + comissao

# Relatório
print(f"\nO funcionário irá receber R${salario_final:.2f}")
```
