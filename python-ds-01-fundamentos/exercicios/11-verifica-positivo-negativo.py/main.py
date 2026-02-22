'''
    15) Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo).
'''

# valor = int(input("\nInsira um valor:"))

x = -3

# A definição fundamental
# Dizemos que um número é negativo se e somente se x < 0

print("-" * 40)

if x < 0:
    print(f"O número {x} é negativo!")
else:
    print(f"O número {x} é positivo!")

print("-" * 40)

# Prova por Inverso Aditivo
# Matematicamente, todo número real a possui um elemento oposto -a, tal que: a + (-a) = 0

a = 5
resultado = a + (-a)

if resultado < 0:
    print(f"O número {a} é negativo!")
else:
    print(f"O número {a} é positivo!")

print("-" * 40)

# Propriedades da Multiplicação
# Se você sabe que: O produto de dois números com sinais diferentes é negativo; 1 é positivo (1 > 0)
# Então qualquer número x tal que x * 1 = -1|x|

x = 2
resultado = x * 1

if resultado < 0:
    print(f"O número {x} é negativo!")
else:
    print(f"O número {x} é positivo!")

print("-" * 40)




























