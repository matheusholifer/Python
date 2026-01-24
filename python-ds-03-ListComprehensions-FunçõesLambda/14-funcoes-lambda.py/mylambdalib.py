"""
    Funções Lambda
    São funções anônimas de uma única linha, criadas com a palavra-chave lambda.
"""

# Uma função que soma 10 ao número recebido
somar_dez = lambda x: x + 10

# Com múltiplos argumentos
multiplicar = lambda a, b: a * b

# Ordanação
velocistas = [("Barry Allen", 30), ("Pietro Maximoff", 26), ("Wally West", 19), ("Vision", 3)]

velocistas_ordenados = sorted(velocistas, key=lambda velocista: velocista[1])

# Funções filter() e map()

numeros = [1, 2, 3, 4, 5, 6]

# map(): Dobrar todos os números
dobro = list(map(lambda x: x * 2, numeros)) # [2, 4, 6, 8, 10, 12]

# filter(): Apenas os números pares
pares = list(filter(lambda x: x % 2 == 0, numeros)) # [2, 4, 6]

# Verifica se é maior de idade
status_idade = lambda idade: "Maior de idade" if idade >= 18 else "Menor de idade"