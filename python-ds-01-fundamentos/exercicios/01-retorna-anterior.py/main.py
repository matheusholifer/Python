'''
    5) Escreva um algoritmo para ler um valor (do teclado) e escrever (na tela) o seu antecessor.
'''

entrada = input("\nDigite algo: ")

if entrada.isdigit():
    valor = int(entrada)
    valor_anterior = valor - 1
    print(f"\n\tO valor anterior a {valor} é = {valor_anterior}")
else:
    try:
        valor = float(entrada)
        valor_anterior = valor - 1.0
        print(f"\n\tO valor anterior a {valor} é = {valor_anterior}")
    except ValueError:
        # Verificando se a entrada é apenas um caractere
        if len(entrada) == 1:
            atual = ord(entrada) # Converte um caractere em seu código numérico
            antecessor = chr(atual - 1) # Transforma o número de volta em caractere
            print(f"\n\tO caractere anterior a '{chr(atual)}' é = '{antecessor}'")
