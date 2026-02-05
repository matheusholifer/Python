import os
import multiprocessing

# É o processo "filho"
def mensagem_filho():
    print(f"\n\tO processo filho (PID {os.getpid()}) está executando...")

    print(f"\n\t\tO processo filho (Pid {os.getpid()}) diz: 'Hello Python World!'.")

    print(f"\n\tO processo filho (PID {os.getpid()}) finalizou com sucesso.")

# É o processo "pai"
def create_process():
    print(f"\nO processo pai (PID {os.getpid()}) está executando...")

    # Cria um novo processo apontando para a função desejada
    p = multiprocessing.Process(target=mensagem_filho)
    p.start()

    # aguarda o filho terminar (Opcional mas boa prática)
    p.join()

    print(f"\nO processo pai (PID {os.getpid()}) finalizou com sucesso.")

# No Windows, é OBRIGATÓRIO usar esse 'if' para evitar loops infinitos
if __name__ == '__main__':
    create_process()