import os
import sys
import threading

def soma_numeros(n, resultado):
    print(f"\n\tThread (TID {threading.get_native_id()}) somando de 1 a {n}...")
    soma = sum(range(1, n + 1))
    resultado.append(soma)
    print(f"\tThread (TID {threading.get_native_id()}) finalizou a soma.")

def thread_soma(n):
    print(f"\nSoma multithread: Cria uma thread para somar os números de 1 a N.")

    print(f"\nValor de N = {n}")

    print(f"\nCriando a thread...")
    print(f"Processo (PID {os.getpid()}) esperando a thread executar...")

    # Criando lista vazia para armazenar o resultado
    resultado = []

    # Criando a thread
    t1 = threading.Thread(target=soma_numeros, args=(n, resultado))

    # Iniciando
    t1.start()

    # O join() faz o programa principal esperar a thread acabar
    t1.join()

    print(f"\nProcesso (PID {os.getpid()}) retoma a execuçaõ e exibe o resultado da soma realizada na thread.")
    print(f"A soma de 1 até {n} = {resultado}")



def main():
    if len(sys.argv) < 2:
        print("\nErro: Você precisa digitar um número.")
        print("\nExemplo: python main.py 10")
        return

    try:
        numero_limite = int(sys.argv[1])

        thread_soma(numero_limite)

    except ValueError:
        print("\nErro: Por favor, insira um número inteiro válido.")

if __name__ == '__main__':
    main()