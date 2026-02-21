Um código introdutório a Files Systems em Python.

```python
import os
import sys
import math


def listar_arquivos(diretorio, extensao):
    if not os.path.isdir(diretorio):
        print("Erro: Diretório não encontrado.")
        return

    unidade_alocacao = 4096

    # Garante que a extensão comece com ponto para comparação
    if not extensao.startswith('.'):
        extensao = '.' + extensao

    # Lista os arquivos no diretório [cite: 18]
    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.lower().endswith(extensao.lower()):
            caminho_completo = os.path.join(diretorio, nome_arquivo)

            tamanho_bytes = os.path.getsize(caminho_completo)
            unidades_usadas = math.ceil(tamanho_bytes / unidade_alocacao)

            print(f"Arquivo: {nome_arquivo}")
            print(f"Tamanho: {tamanho_bytes:,} bytes".replace(',', '.'))
            print(f"Unidades de alocação: {unidades_usadas}")
            print("-" * 20)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        listar_arquivos(sys.argv[1], sys.argv[2])
    else:
        print("Uso: python file-size.py <diretorio> <extensao>")
```
