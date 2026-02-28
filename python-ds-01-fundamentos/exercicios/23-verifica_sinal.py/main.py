'''
    27) Ler um valor e escrever se é positivo, negativo ou zero.
'''
# Coleta de Dados
valor = float(input("\nInsira um valor qualquer: "))

# Prova de Positividade
if valor > 0:
    print("\nNúmero positivo.")
elif valor == 0:
    print("\nZero.")
else:
    print("\nNúmero negativo.")