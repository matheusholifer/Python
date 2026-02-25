Tendo como dados de entrada o nome, a altura e o sexo (M ou F) de uma pessoa, calcule
e mostre seu peso ideal, utilizando as seguintes fórmulas:

- para sexo masculino: peso ideal = (72.7 * altura) - 58
- para sexo feminino: peso ideal = (62.1 * altura) - 44.7

```python
# Coleta de Dados
nome = input("\nInsira o nome da pessoa: ")
altura = float(input("\nInsira a altura da pessoa: (ex: 1.70)"))
while True:
    sexo = input("\nInsira 'M' para masculino ou 'F' para feminino: ").strip().upper()

    if sexo in ('M', 'F'):
        break
    else:
        print(f"\nVocê deve inserir apenas 'M' ou 'F'.")

# Cálculo do peso ideal
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

# Relatório
print(f"\nO peso ideal do(a) paciente {nome}, de altura {altura}m, é = {peso_ideal:.2f}KGs")
```
