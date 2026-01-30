'''
    14) Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso
    contrário escrever NÃO É MAIOR QUE 10!
'''
try:
    # Coleta de dados
    numero = int(input("\nInsira um número inteiro: "))

    # Função lambda para resolver a questão
    maior_que_dez = lambda numero: print(f"\nO número {numero} é maior do que 10!") if numero > 10 else print(f"\nO número {numero} NÃO é maior do que 10!")

    # Relatório
    maior_que_dez(numero)

except ValueError:
    print(f"\nVocê deve inserir um número inteiro!")


