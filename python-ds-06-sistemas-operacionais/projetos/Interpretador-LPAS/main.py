import sys


class InterpretadorLPAS:
    def __init__(self):
        self.memoria_dados = {}  # Armazena variáveis [cite: 74]
        self.registrador = 0  # Único registrador inteiro [cite: 72]
        self.pc = 0  # Contador de programa [cite: 36, 50]
        self.execucao = True  # Controle do loop [cite: 48, 51]

    def rodar(self, programa_lpas):
        # Memória de código (lista de instruções) [cite: 73]
        codigo = [linha.split(';')[0].strip() for linha in programa_lpas if linha.strip() and not linha.startswith(';')]

        print("--- Iniciando Execução LPAS ---")

        while self.execucao and self.pc < len(codigo):
            # 1. Busca [cite: 35, 53]
            instrucao_completa = codigo[self.pc]

            # 2. Atualiza PC [cite: 36, 54]
            self.pc += 1

            # 3 & 4. Decodifica e Localiza Dados [cite: 55, 56]
            partes = instrucao_completa.split()
            cmd = partes[0].upper()
            operando = partes[1] if len(partes) > 1 else None

            # 5 & 6. Busca dados e Executa [cite: 38, 59, 109]
            self.executar(cmd, operando)

    def obter_valor(self, operando):
        """Auxiliar para tratar se o operando é número ou variável."""
        if operando.isdigit() or (operando.startswith('-') and operando[1:].isdigit()):
            return int(operando)
        return self.memoria_dados.get(operando, 0)

    def executar(self, cmd, operando):
        if cmd == "READ":
            self.memoria_dados[operando] = int(input(f"Entrada para {operando}: "))
        elif cmd == "WRITE":
            print(f"Saída: {self.obter_valor(operando)}")
        elif cmd == "LOAD":
            self.registrador = self.obter_valor(operando)
        elif cmd == "STORE":
            self.memoria_dados[operando] = self.registrador
        elif cmd == "ADD":
            self.registrador += self.obter_valor(operando)
        elif cmd == "SUB":
            self.registrador -= self.obter_valor(operando)
        elif cmd == "MUL":
            self.registrador *= self.obter_valor(operando)
        elif cmd == "DIV":
            divisor = self.obter_valor(operando)
            self.registrador //= divisor if divisor != 0 else 1
        elif cmd == "HALT":
            self.execucao = False
            print("--- Programa Finalizado ---")


# Exemplo de uso com o programa de soma do documento [cite: 89-98]
programa = [
    "READ X",
    "READ Y",
    "LOAD X",
    "ADD Y",
    "STORE Z",
    "WRITE Z",
    "HALT"
]

if __name__ == "__main__":
    it = InterpretadorLPAS()
    it.rodar(programa)