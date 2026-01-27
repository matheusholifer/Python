 12) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor
    correspondente em graus Celsius (baseado na fórmula abaixo):

    C / 5 = (F - 32) / 9

```python
# Coleta de dados
temperatura = float(input("\nInsira uma temperatura em graus Fahrenheit para converter em graus Celsius: "))

# Cálculo de fahrenheit para celcius
fahrenheit_celcius = lambda f: (f - 32) * 5 / 9

# Relatório
print(f"\n{temperatura}°F = {fahrenheit_celcius(87):.2f}°C")
```
