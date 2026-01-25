7) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
    dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

```python
idade_dias = lambda a, m, d: (a * 365) + (m * 30) + d

a, m, d = map(int, input("\nInsira sua data de nascimento, no formato (AAAA MM DD): ").split())

print(f"\n\tA sua idade é aproximadamente: {idade_dias(a, m, d)} dias")
```
