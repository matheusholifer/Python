Um código que apresenta a estrutura de funções em python.

- Fatorial de um número (Recursão)

```python

'''
    Função que cálcula o fatorial de um número recursivamente
'''
def fatorial_recursivo(n):
    # Caso base: Fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1

    # Passo recursivo: n! = n * (n - 1)!
    else:
        return n * fatorial_recursivo(n - 1)
```

- Converte um decimal para binário (Recursão)

```python
'''
    Função que converte um número decimal para sua forma binária recursivamente
'''
def decimal_para_binario(n):
    # Caso base 1: Se o número for 0, a representação binária é '0'
    if n == 0:
        return '0'

    # Caso base 2: Se o número for 1, a representação binária é '1'
    elif n == 1:
        return '1'

    # Passo recursivo: binário(quociente) + resto
    # n // 2 é a divisão inteira (quociente)
    # n % 2 é o reto (0 ou 1)
    return decimal_para_binario(n // 2) + str(n % 2) # O operador '//', ao contrário do '%', retorna a parte inteira da divisão
```

- Converte um decimal para hexadecimal (Recursão)

```python
'''
    Função que converte um número decimal para sua forma hexadecimal recursivamente
'''
def decimal_para_hexadecimal(n):
    digitos_hexadecimais = "0123456789ABCDEF"

    # Caso base: Se o número for 0, retorna uma string vazia
    if n == 0:
        return ""

    # Calcula o resto (dígito hexadecimal) e o novo quociente
    resto = n % 16
    quociente = n // 16

    return decimal_para_hexadecimal(quociente) + digitos_hexadecimais[resto]
```

- Converte um decimal para ocatl (Recursão)

```python
'''
    Função que converte um número decimal para sua forma octal
'''
def decimal_para_octal(n):
    # Caso base: Se o número for 0, a recursão para
    if n == 0:
        return ""

    else:
        # Calcula o resto (dígito octal)
        resto = n % 8

        # Passo recursivo: Chama a função com quociente (n // 8) e anexa com o resto da string
        return decimal_para_octal(n // 8) + str(resto) # str() converte um valor para string
```

- Função que tenta emular o comportamento de visualização instantanea da calculadora do windows

```python
'''
    Função que tenta emular a calculadora do windows
'''
def converter_e_exibir(texto_atual):
    # Limpa a tela para dar o efeito de atualização no mesmo lugar
    os.system('cls' if os.name == 'nt' else 'clear')

    print("≡ Programmer")
    print(f"\n\t\t{texto_atual if texto_atual else '0'}\n")
    print("-" * 20)

    if texto_atual.isdigit():
        num = int(texto_atual)

        try:
            res_hex = decimal_para_hexadecimal(num)
            res_oct = decimal_para_octal(num)
            res_bin = decimal_para_binario(num)

            print(f"HEX: {res_hex}")
            print(f"DEC: {num}")
            print(f"OCT: {res_oct}")
            print(f"BIN: {res_bin}")

            if num <= 100:  # Limite seguro para não travar o terminal
                print("-" * 20)
                print(f"FATORIAL: {fatorial_recursivo(num)}")
        except RecursionError:
            print("Erro: Número muito grande para cálculo recursivo.")
    else:
        print("HEX: -\nDEC: -\nOCT: -\nBIN: -")
```
![MSVCRT](https://img.shields.io/badge/msvcrt-blue?style=for-the-badge&logo=visualstudio&logoColor=white)
