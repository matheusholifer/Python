'''
    3. Manipulando CSV (Comma Separated Values)
    O CSV é a linguagem universal das planilhas e da Ciência de Dados. Imagine uma tabela do Excel, mas em formato de texto simples, onde as colunas são separadas por vírgulas (ou ponto e vírgula).

    Para isso, usamos a biblioteca nativa csv.
'''

import csv

# Escrevendo no CSV
dados_produtos = [
    ['ID', 'Nome', 'Preco'], # Cabeçalho
    [1, 'Memória RAM XPG Spectrix D35G, 16GB', 799.99],
    [2, 'SSD Kingston NV3, 1 TB', 849.99],
    [3, 'Smartphone Asus Rog Phone 6', 4499.10],
    [4, 'Samsung Tablet Galaxy Tab S10 Lite', 3964.10]
]

# newline='' é necessário no Windows para não pular linhas extras
with open('produtos.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados_produtos)

# Lendo CSV
with open('produtos.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)

    print(f"{'PRODUTO':<20} | {'PREÇO'}")
    print("-" * 30)

    for linha in leitor:
        print(f"{linha['Nome']:<20} | R$ {linha['Preco']}")