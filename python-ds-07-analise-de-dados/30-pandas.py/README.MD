Um código introdutório a Pandas em Python.

```python
import pandas as pd
import numpy as np
from pandas.conftest import axis
```

```python
# Estruturas de Dados Principais

# Series (Coluna única)
# Criando uma Series a partir de uma lista

notas = pd.Series([8.5, 9.0, 7.5, 10.0], index=['Matemática', 'História', 'Física', 'Química'])
print(notas)
```

```python
# DataFrame (Tabela)

dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernando'],
    'Idade': [28, 30, 32, 27, np.nan, 25], # np.nan representa um dado ausente
    'Departamento': ['TI', 'RH', 'TI', 'Vendas', 'Marketing', 'RH'],
    'Salario': [5500.0, 6200.0, 2000.0, 3500.0, 7500.0, 3500.0]
}

df = pd.DataFrame(dados)
print(df)
```

```python
# Lendo dados (Exemplos)
# df = pd.read_csv('meus_dados.csv')
# df = pd.read_excel('planilha.txt', sheet_name='Aba1')
# df = pd.read_sql('SELECT * FROM tabela', conexao_banco)

# Exportando dados
df.to_csv('dados_exportados.csv', index=False) # index=False evita salvar a voluna de números da linha
```

```python
# Primeiras e últimas linhas
print(df.head(2)) # Mostra as 2 primeiras linhas
print("\n")
print(df.tail(2)) # Mostra as 2 últimas linhas
print("\n")

# Informações gerais (tipos de dados e valores nulos)
print(df.info())
print("\n")

# Resumo estatístico rápido (médio, devio padrão, min, max, etc)
print(df.describe())
print("\n")

# Listar as colunas e os índices
print(df.columns)
print(df.index)
```

```python
# Seleção e Filtragem

# Selecionando Colunas
# Uma coluna (retorna uma Series)
nomes = df['Nome']
print(nomes)
print("\n")

# Múltiplas colunas (retorna um DataFrame)
sub_df = df[['Nome', 'Salario']]
print(sub_df)
print("\n")
```

```python
# Selecionando Linhas (Loc e Iloc)
# Acessando a primeira linha
primeira_linha = df.iloc[0]
print(primeira_linha)
print("\n")

# Filtragem condicional (apenas pessoas de TI)
funcionarios_ti = df.loc[df['Departamento'] == 'TI']
print(funcionarios_ti)
print("\n")

# Múltiplas condições (TI E Salario > 5000)
filtro_avancado = df.loc[(df['Departamento'] == 'TI') & (df['Salario'] > 5000)]
print(filtro_avancado)
print("\n")
```

```python
# Limpeza de Dados (Data Cleaning)

# Lidando com Valores Ausentes (NaN)
# Verificando quantos nulos existem por coluna
print(df.isnull().sum())

# Removendo linhas que contenham qualquer valor nulo
df_limpo = df.dropna()

# Preenchendo valores nulos (ex: preecher idade vazia com a média das idades)
media_idade = df['Idade'].mean()
df['Idade'] = df['Idade'].fillna(media_idade)
```

```python
# Lidando com duplicatas
# Adicionando uma linha duplicada de propósito para o exemplo
df = pd.concat([df, df.iloc[[1]]], ignore_index=True)

# Removendo duplicatas exatas
df = df.drop_duplicates()
```

```python
# Transformação e Criação de colunas

# Operações básicas
# Criando uma nova coluna (Bônus de 10% do salário)
df['Bonus'] = df['Salario'] * 0.10

# deletando uma coluna
df.drop('Bonus', axis=1) # axis=1 significa coluna; axis=0 significa linha
```

```python
# Usando o .apply()

# Função para classificar salários
def classifica_salario(valor):
    if valor > 5500:
        return 'Alto'
    return 'Normal'

# Aplicando a função à coluna
df['Nivel_Salario'] = df['Salario'].apply(classifica_salario)

# Usando função lambda (mesmo resultado, mais rápido para coisas simples)
df['Nome_Maiusculo'] = df['Nome'].apply(lambda x: x.upper() if pd.notnull(x) else x)
```

```python
# Agrupamento e Agregação (Groupby)

# Qual é o salário médio por departamento?
media_por_depto = df.groupby('Departamento')['Salario'].mean()
print(media_por_depto)
print("\n")

# Múltiplas agregações ao mesmo tempo usando .agg()
resumo = df.groupby('Departamento').agg({
    'Salario': ['mean', 'sum'], # Média e soma dos salários
    'Idade': 'max'              # Idade máxima
})
print(resumo)
```

```python
# Combinação de DataFrames (Merge e Concat)

# Concatenação (Empilhar ou colocar lado a lado)
df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})

# Empilhando linhas (um embaixo do outro)
df_empilhado = pd.concat([df1, df2], ignore_index=True)
```

```python
# Merge (Mesclagem tipo SQL/PROCV)
df_funcionarios = pd.DataFrame({'ID': [1, 2, 3], 'Nome': ['Ana', 'Bruno', 'Carlos']})
df_projetos = pd.DataFrame({'ID_Funcionarios': [1, 2, 4], 'Projeto': ['X', 'Y', 'Z']})

# Juntando as tabelas onde o ID bate (INNER JOIN por padrão)
df_completo = pd.merge(df_funcionarios, df_projetos, left_on='ID', right_on='ID_Funcionarios', how='left')
print(df_completo)
```

```python
# Séries Temporais (Manipulação de Datas)
vendas = pd.DataFrame({
    'Data': ['2023-01-01', '2023-01-15', '2023-02-01'],
    'Valor': [100, 150, 200]
})

# Convertendo a coluna 'Data' para o tipo datetime do Pandas
vendas['Data'] = pd.to_datetime(vendas['Data'])

# Agora você pode extrair informações facilmente
vendas['Mes'] = vendas['Data'].dt.month
vendas['Ano'] = vendas['Data'].dt.year
```                                       
