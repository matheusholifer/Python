Um código introdutório a Polimorfismo em Python.

```python
# Duck Typing

class PDF:
    def renderizar(selfself):
        return "Renderizando um documento PDF..."

class HTML:
    def renderizar(self):
        return "Renderizando página HTML..."

# Está função é polimorfica.
# Ela não se importa com a classe, apenas se o objeto tem o método .renderizar()
def mostrar_documento(documento):
    print(documento.renderizar())

# Uso
doc1 = PDF()
doc2 = HTML()

mostrar_documento(doc1) # Saída: Renderizando um documento PDF...
mostrar_documento(doc2) # Saída: Renderizando página HTML...
# Nota: Este é o polimorfismo implícito. É flexível, mas perigoso se você passar um objeto que não tem o método (causará um AttributeError em tempo de execução).

print("-" * 40)

# Polimorfismo por Herança (Method Overriding)

class Pagamento:
    def processar(self):
        # Comportamento padrão (ou genérico)
        raise NotImplementedError("As subclasses devem implementar este método")

class CartaoCredito(Pagamento):
    def processar(self):
        return "Processando pagamento via Cartão de Crédito..."

class Pix(Pagamento):
    def processar(self):
        return "Gerando QR Code do Pix..."

# Função consumidora
def realizar_pagamento(sistema_pgto: Pagamento):
    try:
        print(sistema_pgto.processar())
    except Exception as e:
        print(f"Erro: {e}")

# Uso
pgto1 = CartaoCredito()
pgto2 = Pix()
# pgto3 = Pagamento() # Isso geraria erro ao chamar processar()

realizar_pagamento(pgto1)
realizar_pagamento(pgto2)

print("-" * 40)

# Classes Abstratas (ABCs) - A Segurança

from abc import ABC, abstractmethod

# ABC = Abstract Base Class
class Notificacao(ABC):

    @abstractmethod
    def enviar(self, mensagem: str):
        pass


class Email(Notificacao):
    def enviar(self, mensagem: str):
        print(f"Enviando Email: {mensagem}")


class SMS(Notificacao):
    # Se eu esquecer de implementar 'enviar' aqui,
    # o Python lançará um erro na hora de criar o objeto sms.
    def enviar(self, mensagem: str):
        print(f"Enviando SMS: {mensagem}")


# Uso
email = Email()
email.enviar("Olá!")

# erro = Notificacao() # TypeError: Can't instantiate abstract class...

print("-" * 40)

# Protocolos (O Moderno "Static Duck Typing")

from typing import Protocol, List

# Definimos O QUE o objeto precisa ter, não DE QUEM ele herda.
class Voavel(Protocol):
    def voar(self) -> None:
        ...

class Passaro:
    def voar(self):
        print("O pássaro bate asas.")

class Aviao:
    def voar(self):
        print("O avião liga as turbinas.")

# Note que Passaro e Aviao NÃO herdam de Voavel.
# Mas o type checker sabe que eles cumprem o protocolo.

def iniciar_voo(volante: Voavel):
    volante.voar()

p = Passaro()
a = Aviao()

iniciar_voo(p) # Funciona e passa na checagem de tipos
iniciar_voo(a) # Funciona e passa na checagem de tipos

print("-" * 40)

# Polimorfismo com Métodos Mágicos (Dunder Methods)

class CarrinhoDeCompras:
    def __init__(self, valor):
        self.valor = valor

    # Polimorfismo do operador '+'
    def __add__(self, outro_carrinho):
        return CarrinhoDeCompras(self.valor + outro_carrinho.valor)

    # Polimorfismo da função 'str()' e 'print()'
    def __str__(self):
        return f"Carrinho com total de R$ {self.valor}"

c1 = CarrinhoDeCompras(100)
c2 = CarrinhoDeCompras(50)

# O Python traduz isso para: c1.__add__(c2)
c3 = c1 + c2

print(c3) # Saída: Carrinho com total de R$ 150

```
