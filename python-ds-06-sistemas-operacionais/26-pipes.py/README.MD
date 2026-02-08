Um código introdutório a Comunicação entre Processos em Python.

```python
import os
import sys
from multiprocessing import Process, Pipe

def calcula_fibonnacci(n, conn):
    print(f"\n\tO processo filho (PID {os.getpid()}) está gerando a sequência...")

    if n <= 0:
        fib = []
    elif n == 1:
        fib = [0]
    else:
        fib = [0, 1]
        while len(fib) < n:
            proximo = fib[-1] + fib[-2]
            fib.append(proximo)

    # Envia os dados pelo pipe
    conn.send(fib)
    conn.close()

    print(f"\tO processo filho (PID {os.getpid()}) finalizou com sucesso.")

def pipe_fibonacci(n):
    print(f"\nO processo pai (PID {os.getpid()}) está executando...")

    # Criamos o Pipe. Ele retorna dois objetos de conexão.
    lado_pai, lado_filho = Pipe()

    # Criamos o processo filho passando o lado dele do pipe
    p = Process(target=calcula_fibonnacci, args=(n, lado_filho))
    p.start()

    # O pai recebe a informação enviada pelo filho
    # recv() bloqueia a execução até que algo chegue
    sequencia = lado_pai.recv()

    p.join()

    print(f"\nSequência de Fibonacci: {sequencia}")

    print(f"\nO processo pai (PID {os.getpid()}) finalizou com sucesso.")

def main():
    if len(sys.argv) < 2:
        print("\nErro: Você precisa digitar um número.")
        print("Exemplo: python seu_arquivo.py 10")
        return

    try:
        numero_limite = int(sys.argv[1])
        pipe_fibonacci(numero_limite)
    except ValueError:
        print("\nErro: Por favor, insira um número inteiro válido.")

if __name__ == '__main__':
    main()
```
