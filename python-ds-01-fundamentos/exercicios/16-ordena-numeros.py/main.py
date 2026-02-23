'''
    20) Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.
'''

lista = [] # Lista vazia para armazenar os números

while True:
    try:
        a = float(input("\nEnter the first number:"))
        b = float(input("\nEnter the second number:"))

        if a != b:
            lista.append(a)
            lista.append(b)
            break

        print("\n\tYou must enter two different numbers.")

    except:
        print("\n\tError: Please enter only numeric values (use '.' for decimals).")

# Ordena os elementos da lista
lista.sort()

print(f"\n{lista=}")