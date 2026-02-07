import os
import sys
import platform
import subprocess
import readline  # Biblioteca chave para o Tab
import glob      # Ajuda a listar arquivos

# Códigos ANSI para cores
RESET = "\033[0m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
VERMELHO = "\033[31m"
NEGRITO = "\033[1m"

# Lista de comandos para o autocomplete
COMANDOS = ['cd', 'dir', 'python', 'exit', 'quit', 'cls']

def completador(text, state):
    """
    Busca comandos internos e arquivos/pastas.
    """
    # 1. Sugestões de comandos internos
    opcoes = [c for c in COMANDOS if c.startswith(text)]

    # 2. Sugestões de arquivos e pastas (usando glob)
    # Adicionamos o que o glob encontrar à nossa lista de opções
    arquivos = glob.glob(text + '*')
    for f in arquivos:
        if os.path.isdir(f):
            opcoes.append(f + os.sep)  # Adiciona barra se for pasta
        else:
            opcoes.append(f)
    try:
        return opcoes[state]
    except IndexError:
        return None


# Configurações do readline
readline.set_completer(completador)
readline.parse_and_bind("tab: complete")
# Esta é a linha mágica para o Ctrl + L:
readline.parse_and_bind('Control-l: clear-screen')
# Garante que o Tab funcione mesmo com espaços e caminhos
readline.set_completer_delims(' \t\n`@=#%&+{[|;,"\'')

def shell():
    # Diretório onde estão os scripts
    diretorio_alvo = "C:\\Users\\Matheus\\Documents\\MatheusFerreira\\Python"

    try:
        if os.path.exists(diretorio_alvo):
            os.chdir(diretorio_alvo)
        else:
            print(f"\n{AMARELO}Aviso: Diretório '{diretorio_alvo}' não encontrado. Usando atual.{RESET}")
    except Exception as e:
        print(f"{VERDE}Erro: Não foi possível abrir o diretório {e}{RESET}")

    print(f"{VERDE}{NEGRITO}--- Python Custom Shell [S.O. {platform.system()}] ---{RESET}")
    print(f"{AZUL}{NEGRITO}- Por Matheus Holifer -{RESET}")

    while True:
        prompt = f"\n{VERDE}>>> {RESET}"
        entrada = input(prompt).strip()

        if entrada.lower() in ['exit', 'quit']:
            break

        if not entrada:
            continue

        partes = entrada.split()
        comando = partes[0].lower()
        argumentos = partes[1:]

        try:
            if comando == 'cd':
                if argumentos:
                    novo_caminho = " ".join(argumentos)
                    os.chdir(novo_caminho)

                else:
                    print(f"{os.getcwd()}")

            else:
                subprocess.run(entrada, shell=True)

        except FileNotFoundError:
            print(f"{VERMELHO}Erro: O arquivo ou comando '{entrada}' não foi encontrado.{RESET}")

        except Exception as e:
            print(f"{VERMELHO}Erro na execução: {e}{RESET}")

if __name__ == '__main__':
    shell()















