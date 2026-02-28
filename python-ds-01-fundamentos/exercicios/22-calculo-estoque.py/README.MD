26) Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e
quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade
média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual
a quantidade média escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar
compra'.

```python
# Coleta de Dados
quantidade_atual = int(input("\nInsira a quantidade atual em estoque: "))
quantidade_mínima = int(input("\nInsira a quantidade mínima em estoque: "))
quantidade_máxima = int(input("\nInsira a quantidade máxima em estoque: "))

# Cálculo da Quantidade Média em estoque
quantidade_media = (quantidade_máxima + quantidade_mínima) / 2

# Relátorio Final
if quantidade_atual >= quantidade_media:
    print("\nNão efetuar compra!")
else:
    print("\nEfetuar compra!")
```
