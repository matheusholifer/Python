Um código simples, que explica como usar listas (do Python) como pilhas. Segue o padrão (LIFO - Last In, First Out).

```python
def esta_balanceado(expressao):
    pilha = []

    # Dicionário para mapear o fechamento com a abertura
    mapeamento = {')': '(', ']': '[', '}': '{'}

    for caractere in expressao:
        # Se for símbolo de abertura, "empilha"
        if caractere in mapeamento.values(): # É usado em dicionários para retornar uma "visão" (view object) de todos os valores contidos nele
            pilha.append(caractere)

        # Se for símbolo de fechamento
        elif caractere in mapeamento.keys():
            # Se a pilha estiver vazia ou o topo não corresponder ao par
            if not pilha or pilha.pop() != mapeamento[caractere]:
                return False

    # Se ao final a pilha estiver vazia, tudo foi fechado corretamente
    return len(pilha) == 0

expressao1 = "[({})]"
expressao2 = "[]{)(}"

print(f"\nThe expression '{expressao1}' {'is balanced.' if esta_balanceado(expressao1) else 'isn\'t balanced.'}")

print(f"\nThe expression '{expressao2}' {'is balanced.' if esta_balanceado(expressao2) else 'isn\'t balanced.'}")
```

- Note que no código, o dicionário associa chaves (fechamento) a valores (abertura). .values() acessa os símbolos de abertura (['{ para empilhar. .keys() identifica os de fechamento; quando um é achado, o código usa a chave para buscar o valor correspondente no dicionário e validar o topo da pilha via .pop().
