25) Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e
escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior
ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

```python
# Coleta de Dados
numero_conta = int(input("\nInsira o número da conta do cliente: "))
saldo = float(input("\nInsira o saldo atual em conta: "))
debito = float(input("\nInsira o débito atual em conta: "))
credito = float(input("\nInsira o credito atual em conta: "))

# Cálculo do Saldo Atual
saldo_atual = saldo - debito + credito

# Status
status = 'saldo positivo' if saldo_atual >= 0 else 'saldo negativo'

# Relatório
print(f"\nO clinte (Conta: {numero_conta}) tem {status}.")
```
