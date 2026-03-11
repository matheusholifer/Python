    35) Um posto está vendendo combustíveis com a seguinte tabela de descontos:

                • até 20 litros, desconto de 3% por litro
    -> Álcool
                • acima de 20 litros, desconto de 5% por litro

                • até 20 litros, desconto de 4% por litro
    -> Gasolina
                • acima de 20 litros, desconto de 6% por litro

    Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da
    seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
    que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90.

```python
# Coleta de Dados
tipo_combustivel = input("\nInsira 'A' para álcool, ou 'G' para gasolina: ").upper()

# Enquanto o que foi digitado NÃO estiver na lista permitida...
while tipo_combustivel not in ['A', 'G']:
    print("Entrada inválida! Por favor, use apenas 'A' ou 'G'.")
    tipo_combustivel = input("Insira 'A' para álcool, ou 'G' para gasolina: ").upper()

litros_vendidos = float(input("\nInsira o total de litros vendidos: "))

# Cálculo do Preço do Combustível
if tipo_combustivel == 'A':
    preco_litro = 2.90
    if litros_vendidos <= 20:
        porcentual_desconto = 0.03
    else:
        porcentual_desconto = 0.05

    valor_total = litros_vendidos * (preco_litro * (1 - porcentual_desconto))

elif tipo_combustivel == 'G':
    preco_litro = 3.30
    if litros_vendidos <= 20:
        porcentual_desconto = 0.04
    else:
        porcentual_desconto = 0.04

    valor_total = litros_vendidos * (preco_litro * (1 - porcentual_desconto))

# Relatório Final
print(f"\nO cliente deverá pagar R${valor_total:.2f} pelos {litros_vendidos}L de {'álcool' if tipo_combustivel == 'A' else 'gasolina'}.")
```
