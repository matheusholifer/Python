30) Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

```python
valores = set()
print("\nInsira 3 números diferentes")
while len(valores) < 3:
    try:
        entrada = int(input(f"\nInsira o {len(valores) + 1}° número: "))
        if entrada in valores:
            print("\nValor repetido! Tente um número diferente.")
        else:
            valores.add(entrada)  # Se for repetido o set ignora

    except ValueError:
        print("\nVocê deve inserir um número inteiro!")

# Converte para lista ordenando
resultado = sorted(list(valores))

print(f"\nValores em ordem crescente: {resultado}")
```
