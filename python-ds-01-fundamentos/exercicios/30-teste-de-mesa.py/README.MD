    34) Seja o seguinte algoritmo:

    inicio
        ler x
        ler y

        z = (x * y) + 5

        se z <= o então
            resposta 'A'
        senão
            se z <= 100 então
                resposta 'B'
            senão
                resposta 'C'
            fim_se
        fim_se

        escrever z, resposta
    fim

    Faça um teste de mesa e complete o quadro a seguir:

    | X   | Y  | Z   | RESPOSTA |
    |-----|----|-----|----------|
    | 3   | 2  | 11  | B        |
    | 150 | 3  | 455 | C        |
    | 7   | -1 | -2  | A        |
    | -2  | 5  | -5  | A        |
    | 50  | 3  | 155 | C        |

```python
x = int(input("\nInsira o valor de 'x': "))
y = int(input("\nInsira o valor de 'y': "))

z = (x * y) + 5

if z <= 0:
    resposta = 'A'
else:
    if z <= 100:
        resposta = 'B'
    else:
        resposta = 'C'

print(f"\n{z=}, {resposta=}")
```
