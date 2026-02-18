Um código introdutório a Matplotlib em Python.

```python
import matplotlib.pyplot as plt
import numpy as np

# Gráfico de linhas (Line Plot)

# Preparando os dados
x = np.linspace(0, 10, 100) # 100 pontos espaçados entre 0 e 10
y = x ** 2                   # y = x^2

# Criando o gráfico
plt.plot(x, y, color='blue', linewidth=2, label='Curva y = x²')

# Adicionando títulos e rótulos
plt.title('Meu Primeiro Gráfico de Linhas')
plt.xlabel('Eixo X (Tempo ou Unidades)')
plt.ylabel('Eixo Y (Valores)')

# Exibindo a legenda e o gráfico
plt.legend()
plt.show()

# Gráfico de Dispersão (Scatter Plot)

# Gerando dados aleatórios
x = np.random.rand(50)
y = np.random.rand(50)
cores = np.random.rand(50) # Cores aleatórias para cada ponto
tamanhos = 1000 * np.random.rand(50) # Tamanhos aleatórios

plt.scatter(x, y, c=cores, s=tamanhos, alpha=0.5, cmap='viridis')

plt.title('Gráfico de Dispersão (Scatter Plot)')
plt.xlabel('Variável X')
plt.ylabel('Variável Y')
plt.colorbar(label='Intensidade da Cor') # Adiciona uma barra de cores lateral

plt.show()

# Gráfico de Barras (Bar Chart)

categorias = ['Maças', 'Bananas', 'Laranjas', 'Uvas']
quantidades = [25, 40, 30, 15]

# Gráfico de barras verticais
plt.bar(categorias, quantidades, color=['red', 'yellow', 'orange', 'purple'])

plt.title('Estoque de Frutas')
plt.xlabel('Tipos de Frutas')
plt.ylabel('Quantidade em Kg')

# Adicionando valores em cima de cada barra
for i, valor in enumerate(quantidades):
    plt.text(i, valor + 1, str(valor), ha='center', fontweight='bold')

plt.show() # Se quiser barras horizontais, basta usar plt.barh() no lugar de plt.bar().

# Histogramas (Distribuindo Frequências)

# Gerando dados com uma distribuição normal (média 50, desvio padrão 10)
dados = np.random.normal(50, 10, 1000)

# O parâmetro 'bins' define em quantas "caixas" os dados serão divididos
plt.hist(dados, bins=30, color='skyblue', edgecolor='black')

plt.title('Distribuição Normal (Histograma)')
plt.xlabel('Valores')
plt.ylabel('Frequência')

plt.show()

# Gráfico de Pizza (Pie Chart)

fatias = [35, 25, 20, 20]
labels = ['Frontend', 'Backend', 'Data Science', 'DevOps']
destaque = [0.1, 0, 0, 0] # "Puxa" a primeira fatia (Frontend) para fora

plt.pie(fatias, labels=labels, explode=destaque, autopct='%1.1f%%', shadow=True, startangle=90)

plt.title('Distribuição de Vagas de TI')
plt.axis('equal') # Garante que o gráfico seja um círculo perfeito

plt.show()

# Subplots: A Abordagem Orientada a Objetos

x = np.linspace(0, 2 * np.pi, 100)

# Cria uma figura e uma matriz de eixos (2 linhas e 1 coluna)
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))

# Gráfico 1 (no topo)
ax1.plot(x, np.sin(x), color='green', linestyle='--')
ax1.set_title('Função Seno')
ax1.grid(True) # Adiciona a grade ao fundo

# Gráfico 2 (na base)
ax2.plot(x, np.cos(x), color='red', marker='o', markersize=4, linestyle='')
ax2.set_title('Função Cosseno')
ax2.set_xlabel('Ângulo (radianos)')
ax2.grid(True)

# Ajusta o layout para não sobrepor os textos
plt.tight_layout()
plt.show()

# Salvando o Gráfico

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y, marker='X', color='purple')
plt.title('Gráfico de Vendas')

# Salvando a imagem com alta resolução (dpi=300) e fundo transparente
plt.savefig('meu_grafico_vendas.png', dpi=300, transparent=True)
print("Gráfico salvo com sucesso!")
```
