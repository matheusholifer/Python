1) Crie uma lista com 5 números inteiros e imprima a soma deles.

```python
# Cria uma lista vazias
lista = []
contador = 1

# Coleta os dados
while len(lista) < 5:
    try:
        elemento = int(input(f"\nInsira o {contador}° número inteiro: "))
        lista.append(elemento)
        contador += 1
    except ValueError:
        print("\nVocê deve inserir um número inteiro!")

# Soma os elementos da lista
soma1 = sum(lista) # utilizando sum

soma2 = 0
for elemento in lista:
    soma2 += elemento # Utilizando for (É mais útil caso seja necessário aplicar lógica condicional)

# Relatório
print("\nOs elementos foram inseridos na lista com sucesso!")
print(f"\n\t{lista=}")

print(f"\n\tA soma = " + str(soma2))
```
