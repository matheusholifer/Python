19) Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles. 

```python
'''
    19) Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.
'''
while True:
    try:
        a = float(input("\nEnter the first number: "))
        b = float(input("\nEnter the second number: "))

        if a != b:
            break

        print("\n\tYou must enter two different numbers.")
    except:
        print("\n\tError: Please enter only numeric values (use '.' for decimals).")

# O método da diferença
# Se a - b > 0, então a > b
# Se a - b < 0, então a < b
# Se a - b = 0, então a = b

if (a - b) > 0:
    print(f"\n{a} > {b}")
elif (a - b) < 0:
    print(f"\n{a} < {b}")
else:
    print(f"\n{a} = {b}") # Para o enunciado, foi implementado um loop que garanta a inexistência de números repetidos
```
