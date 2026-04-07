'''
    42) Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. Para
    estar em condições, um dos seguintes requisitos deve ser satisfeito:

        - Ter no mínimo 65 anos de idade.
        - Ter trabalhado no mínimo 30 anos.
        - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.

    Com base nas informações acima, faça um algoritmo que leia: o número do empregado (código), o ano
    de seu nascimento e o ano de seu ingresso na empresa. O programa deverá escrever a idade e o tempo
    de trabalho do empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'.
'''

'''
    d) Para cada empregado cadastrado, salve suas informações (código, idade, tempo de serviço e status) em um dicionário e adicione esse dicionário a uma lista chamada folha_pagamento.
'''

# Inicialização da lista e contador
folha_pagamento = []
proximo_codigo = 1

'''
    c) Coloque a lógica dentro de um laço while. O programa deve perguntar "Deseja cadastrar outro empregado? (S/N)" e continuar rodando até que o usuário decida parar.
'''
while True:
    print("-" * 30)
    print("SISTEMA DE REQUERIMENTO DE APOSENTADORIA")


    '''
        b) Importe o módulo datetime do Python e use-o para capturar o ano atual do sistema operacional.
    '''
    import datetime as dt

    # Captura a data e a hora completa do sistema
    data_atual = dt.datetime.now()

    # extrai apenas o ano
    ano_atual = data_atual.year

    # Entrada de Dados
    codigo_empregado = input("\nInsira o número do empregado (Código): ")

    '''
    a) Use um bloco try-except para garantir que ano_nascimento e ano_ingresso sejam números inteiros válidos. Se o usuário errar, peça o dado novamente.
    '''
    while True:
        try:
            ano_nascimento = int(input("\nInsira o ano de nascimento do empregado: "))
            ano_ingresso = int(input("\nInsira o ano em que o funcionário ingressou na empresa: "))
            # Se as conversões acima funcionarem, o código continua para a próxima linha
            break # Sai do loop pois o valor é válido
        except ValueError:
            # Se o úsuario inserir valores não númericos, o python pula direto para cá
            print("Entrada inválida! Digite apenas números inteiros!")

    # Cálculos iniciais
    idade = ano_atual - ano_nascimento
    tempo_trabalho = ano_atual - ano_ingresso

    # Regra de negócio simples para o Status
    status = "Ativo" if idade < 65 else "Aposentável"

    # Criando o dicionário do empregado_atual
    empregado = {
        "codigo": proximo_codigo,
        "idade": idade,
        "tempo_trabalho": tempo_trabalho,
        "status": status
    }

    # Adicionando o dicionário à lista global
    folha_pagamento.append(empregado)
    print(f"Empregado {proximo_codigo} adicionado com sucesso!")

    # Incrementa o próximo código
    proximo_codigo += 1

    # Saída das informações básicas
    print(f"\nEmpregado: {codigo_empregado}")
    print(f"Idade: {idade} anos")
    print(f"Tempo trabalhado: {tempo_trabalho} anos")

    # Verificação dos requisitos
    if idade >= 65:
        print("Mensagem: Requerer aposentadoria")
    elif tempo_trabalho >= 30:
        print("Mensagem: Requerer aposentadoria")
    elif idade >= 60 and tempo_trabalho >= 25:
        print("Mensagem: Requerer aposentadoria")
    else:
        print("Mensagem: Não requerer")

    # Controle de saída do laço
    opcao = input("\nDeseja cadastrar outro empregado? (S/N): ").strip().upper()
    if opcao == 'N':
        print("\nEncerrando o sistema...")
        break
    elif opcao != 'S':
        print("Opção inválida, mas assumindo que deseja continuar...")

print("-" * 30)
print(f"RELATÓRIO FINAL: {len(folha_pagamento)} empregados em memória.")
for emp in folha_pagamento:
    print(emp)
