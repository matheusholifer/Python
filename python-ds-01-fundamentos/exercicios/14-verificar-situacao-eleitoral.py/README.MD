18) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela
    poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

```python
# Coleta de Dados
entrada = input("\nInsira o ano atual e o nascimento (ex: 2024, 2000): ")
ano_atual, ano_nascimento = map(int, entrada.split(', '))

idade = ano_atual - ano_nascimento

# Lógica: Voto obrigatório é apenas entre 18 e 69 anos
verificar_voto = lambda i: "Voto OBRIGATÓRIO." if 18 <= i < 70 else "Voto NÃO OBRIGATÓRIO ou FACULTATIVO."

# Relatório
print(f"\nIdade: {idade} anos")
print(verificar_voto(idade))
```
