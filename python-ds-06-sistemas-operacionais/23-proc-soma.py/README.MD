Um código introdutório a argv em Python.

```python
import os
import sys
import multiprocessing

def soma_numeros(n):
    print(f"\n\tO processo filho (PID {os.getpid()}) está somando os números de 1 ate {n}...")

    soma = sum(range(1, n + 1))

    print(f"\n\t\tA soma = {soma}")

    print(f"\n\tO processo filho (PID {os.getpid()}) finalizou com sucesso.")

def proc_soma(n):
    print(f"\nO processo pai (PID {os.getpid()}) está executando...")

    p = multiprocessing.Process(target=soma_numeros, args=(n,))
    p.start()

    p.join()

    print(f"\nO processo pai (PID {os.getpid()}) finalizou com sucesso.")

def main():
    if len(sys.argv) < 2:
        print("Erro: Você precisa digitar um número.")
        print("Exemplo: python main.py 10")
        return

    try:
        numero_limite = int(sys.argv[1])

        proc_soma(numero_limite)

    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")

if __name__ == '__main__':
    main()
```
