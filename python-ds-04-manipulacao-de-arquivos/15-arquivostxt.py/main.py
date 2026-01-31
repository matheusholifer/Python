'''
    with open('caminho_do_arquivo', 'modo') as variavel:

        'r' (Read): Apenas leitura. O arquivo deve existir.
        'w' (Write): Escrita. Cuidado: Apaga tudo o que estava lá antes. Cria o arquivo se não existir.
        'a' (Append): Adicionar. Escreve no final do arquivo sem apagar o conteúdo antigo.
'''

notas = [ # Receita de pizza do S.T.A.R labs
    "Barry Allen é o segundo Flash da DC Comics.",
    "Investigador forense, ganhou supervelocidade após ser atingido por um raio e produtos químicos.",
    "Membro da Liga da Justiça, ele usa a Força de Aceleração para proteger Central City e viajar no tempo.",
    "É o herói mais rápido do mundo."
]

# Escrevendo em um arquivo txt
with open('barryallen.txt', 'w', encoding='utf-8') as arquivo:
    for nota in notas:
        arquivo.write(nota + '\n') # Escreve cada nota no arquivo recém criado

# Lendo o arquivo txt que criamos
with open('barryallen.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read() # Lê o arquivo inteiro de uma vez
        print(conteudo)

'''
    Dica: Ler arquivo linha a linha (melhor para arquivos gigantes)
    
    with open('diario.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(f"Lendo: {linha.strip()}") # strip() remove o \n extra
'''

# Novas notas para adicionar (Append)
novas_notas = [
    "Ele é o fundador dos Laboratórios STAR em algumas cronologias.",
    "Sua esposa é Iris West.",
    "Barry causou o Flashpoint ao tentar salvar sua mãe."
]

# Usando 'a' para adicionar ao final do arquivo barryallen.txt
with open('barryallen.txt', 'a', encoding='utf-8') as arquivo:
    for nota in novas_notas:
        arquivo.write(nota + '\n')

# Lendo novamente para ver o resultado completo
with open('barryallen.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())