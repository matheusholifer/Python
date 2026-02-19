Um código introdutório a Seaborn em Python.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Vamos carregar um dataset famoso chamado "tips" (gorjetas)
dados = sns.load_dataset("tips")

# Ver as primeiras linhas para entender o que temos
print(dados.head())

# Gráficos de relacionamentos (Relational Plots)

# Gráfico de dispersão (Scatter Plot)
# Queremos ver se o total da conta (total_bill) influencia na gorjeta (tip)
'''
    hue="day": Colore os pontos de acordo com o dia da semana.

    style="time": Muda o formato do ponto (bolinha ou xis) baseado no horário (Almoço/Jantar).

    size="size": O tamanho do ponto varia conforme o número de pessoas na mesa.
'''
sns.relplot(data=dados, x="total_bill", y="tip", hue="day", style="time", size="size")
plt.show()

# Gráfico de linha (Line Plot)

# Vamos usar outro dataset interno de voos
voos = sns.load_dataset("flights")

sns.relplot(data=voos, x="year", y="passengers", kind="line")
plt.show()

# Distribuição dos dados (Distribution Plots)

# Histograma e KDE
# Mostra a distribuição do valor das contas

'''
    O displot() mostra a frequência dos valores.

    kde=True: Adiciona aquela linha suave (Kernel Density Estimate) que mostra a densidade.
'''
sns.displot(data=dados, x="total_bill", kde=True, color="purple")
plt.show()

# Dados Categóricos (Categorical Plots)

# Boxplot (Gráfico de Caixa)
sns.catplot(data=dados, x="day", y="total_bill", kind="box", palette="Set2", hue="day", legend=False)
plt.show()

# Bar Plot (Gráfico de Barras)

sns.catplot(data=dados, x="sex", y="total_bill", kind="bar", hue="smoker")

# Visualizando matrizes (Heatmaps)

# Calculamos a correlação (apenas valores númericos)
corr = dados.select_dtypes(include='number').corr()

# Criamos o mapa de calor
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

# Estética e Temas

# Escolha um tema: "whitegrid", "dark", "ticks"
sns.set_theme(style="darkgrid")

sns.violinplot(data=dados, x="day", y="total_bill")
plt.show()
```

- Um resumo abaixo:

Função | O que faz?
----- | -----
sns.relplot() | Gráficos de relação (dispersão/linha).
sns.displot() | Distribuições (histogramas).
sns.catplot() | Comparações entre categorias (barras, caixas, violino).
sns.jointplot() | Compara duas variáveis e mostra a distribuição de ambas ao mesmo tempo.
sns.pairplot() | Faz um "raio-x" de todo o seu dataset, cruzando todas as colunas.
