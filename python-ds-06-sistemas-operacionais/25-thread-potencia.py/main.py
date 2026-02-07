import os
import sys
import threading

RESET = "\033[0m"
VERDE = "\033[32m"
AZUL = "\033[34m"

def calcula_potencias(n, potencias):
    print(f"\n{AZUL}Thread Potencia (TID {threading.get_native_id()}) calculando as potencias...{RESET}")

    for i in range(n):
        potencias.append(2 ** i)

    print(f"{AZUL}Thread Potencia (TID {threading.get_native_id()}) finalizou.{RESET}")

def soma_potencias(n, potencias, resultado):
    print(f"\n{AZUL}Thread Soma (TID {threading.get_native_id()}) somando as potencias...{RESET}")

    valor_soma = sum(potencias)
    resultado.append(valor_soma)

    print(f"{AZUL}Thread Soma (TID {threading.get_native_id()}) finalizou.{RESET}")

def main():
    if len(sys.argv) < 2:
        print("\nErro: Você precisa digitar um número.")
        print("\nExemplo: python main.py 10")
        return

    try:
        numero_limite = int(sys.argv[1])

        print(f"\n{VERDE}- Soma de potências multithread{RESET}")
        print(f"\nProcesso (PID {os.getpid()}) esperando a Thread Potencia executar...")

        lista_potencias = []
        resultado_soma = []

        t1 = threading.Thread(target=calcula_potencias, args=(numero_limite, lista_potencias))
        t1.start()
        t1.join()

        print(f"\nProcesso (PID {os.getpid()}) retoma a execução...")
        print(f"Processo (PID {os.getpid()}) esperando a Thread Soma executar...")

        t2 = threading.Thread(target=soma_potencias, args=(numero_limite, lista_potencias, resultado_soma))
        t2.start()
        t2.join()

        print(f"\nProcesso (PID {os.getpid()}) retoma a execução...")

        print(f"\n{VERDE} - A soma = {resultado_soma}{RESET}")



    except ValueError:
        print("\nErro: Por favor, insira um número inteiro válido.")

if __name__ == '__main__':
    main()