37) Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                    Até 5KG          Acima de 5KG
    Morango     R$ 2.50 por KG      R$ 2.20 por KG
    Maça        R$ 1.80 por KG      R$ 1.50 por kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá
    ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de
    morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

```python
# Coleta de Dados
morangos_comprados = float(input("\nInsira a quantidade de morangos que foram comprados em KGs: "))
macas_compradas = float(input("\nInsira a quantidade de macas que foram compradas em KGs: "))

# Cálculo do Preço dos Morangos
if morangos_comprados <= 5:
    valor_morangos = morangos_comprados * 2.50
else:
    valor_morangos = morangos_comprados * 2.20

# cálculo do preço das Maças
if macas_compradas <= 5:
    valor_macas = macas_compradas * 1.80
else:
    valor_macas = macas_compradas * 1.80

# Totais para Verificação de Desconto
peso_total = morangos_comprados + macas_compradas
valor_bruto = valor_morangos + valor_macas

# Aplicação do Desconto de 10% (Se atingir os critérios)
if peso_total > 8 or valor_bruto > 25:
    valor_final = valor_bruto * 0.90
else:
    valor_final = valor_bruto

# Relatório
print(f"\n Valor a ser pago: R$ {valor_final:.2f}")
```
