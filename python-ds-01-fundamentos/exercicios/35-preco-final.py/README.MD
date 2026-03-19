40) Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço
unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total
a pagar (total a pagar = total - desconto), sabendo-se que:
- Se quantidade <= 5 o desconto será de 2%
- Se quantidade > 5 e quantidade <=10 o desconto será de 3%
- Se quantidade > 10 o desconto será de 5%

```python
# Coleta de Dados
nome_produto = input("\nEnter the product name: ")
quantidade_adquirida = int(input("\nEnter the quantity purchased: "))
preco_unitario = float(input("\nEnter the unit price: "))

# Cálculo do preço final
total = quantidade_adquirida * preco_unitario
if quantidade_adquirida > 0 and quantidade_adquirida <= 5:
    desconto = total * (2.0 / 100)
    total_a_pagar = total - desconto
elif quantidade_adquirida > 5 and quantidade_adquirida <= 10:
    desconto = total * (3.0 / 100)
    total_a_pagar = total - desconto
else:
    desconto = total * (5.0 / 100)
    total_a_pagar = total - desconto

# relatório
print(f"\nO preço final que o cliente deve pagar por {quantidade_adquirida}x de {nome_produto} é R${total_a_pagar:.2f}")
```
