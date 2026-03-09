'''
    33) Ler dois valores e imprimir uma das três mensagens a seguir:
    ‘Números iguais’, caso os números sejam iguais
    ‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
    ‘Segundo maior’, caso o segundo seja maior que o primeiro.
'''
# Coleta de Dados
a, b = map(float, input("\nInsira dois números (iguais ou diferentes), separados por espaço e vírgula: ").split(" ,"))

# Descobrindo igualdade ou diferença
status = a - b

# Relatório
if status == 0:
    print(f"\nOs números {a=} e {b=} são iguais.")
elif status < 0: # Se o resultado da subtração for um inteiro negativo, 'b' > 'a'
    print(f"\nO número {b=} é MAIOR que {a=}.")
else:
    print(f"\nO número {a=} é MAIOR que {b=}.")
