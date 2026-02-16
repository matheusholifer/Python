Um código Jupyter Notebook introduzindo o uso de Numpy em Python.

```python
import numpy as np
import sys

# Comparação de memória
lista = list(range(1000))
array = np.arange(1000)

print(f"Memória da lista: {sys.getsizeof(lista)} bytes")
print(f"Memória do array: {array.nbytes} bytes")
```

```python
# 1. De uma lista
array1 = np.array([1, 2, 3])

# 2. Matriz 2D (Linhas e colunas)
array2 = np.array([[1, 2, 3], [4, 5, 6]])

# 3. Arrays automáticos
zeros = np.zeros((3, 3)) # Matriz 3x3 de zeros
uns = np.ones((2, 4)) # Matriz 2x4 de uns
espacados = np.linspace(0, 10, 5) # 5 números de 0 a 10 igualmente espaçados
identidade = np.eye(4) # Matriz identidade 4x4
```

```python
print("-" * 40)

print(f"\nArray de uma lista:\n\n\t{array1}")

print(f"\nMatriz 2D:\n\n{array2}")

print(f"\nMatriz 3x3 de zeros:\n\n{zeros}")

print(f"\nMatriz 2x4 de uns:\n\n{uns}")

print(f"\n5 números de 0 a 10 igualmente espaçados:\n\n\t{espacados}")

print(f"\nMatriz identidade 4x4:\n\n{identidade}\n")

print("-" * 40)
```

```python
# Inspeção de atributos

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.ndim) # Número de dimensões (2)
print(arr.shape) # Formato (2 linhas, 3 colunas)
print(arr.size) # Total de elementos (6)
print(arr.dtype) # Tipo de dado (int64, float64, etc)
```

```python
# Manipulação: Slicing e Indexação

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(arr)

# Selecionar um elemento [linha, coluna]
print(arr[0, 1]) # 20

# Slicing (Fatiamento)
# Pegar a primeira coluna inteira
print(arr[:, 0])

# Pegar uma sub-matriz (2x2 do canto superior)
print(arr[0:2, 0:2])
```

```python
# Operações matemáticas (Broadcasting)

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# Operações básicas
print(a + b) # [11, 22, 33]
print(a * 2) # [2, 4, 6]
print(a ** 2) # [1, 4, 6]

# Funções universais (ufuncs)
print(np.sin(a)) # [0.84147098 0.90929743 0.14112001]
print(np.exp(a)) # [ 2.71828183  7.3890561  20.08553692]
print(np.sqrt(b)) # [3.16227766 4.47213595 5.47722558]

```

```python
# Reshaping

linear = np.arange(12) # [0, 1, 2... 11]

# Transformar em 3 linhas e 4 colunas
matriz = linear.reshape(3, 4)

# Achatar de volta (Flatten)
original = matriz.ravel()
```

```python
# Agregação e estátistica

sequencia = np.arange(1, 10, 2) # [1 3 5 7 9]

print(f"\nA soma dos números na sequência é = {sequencia.sum()}")

print(f"\nA média aritmética dos números na sequência é = {sequencia.mean()}")

print(f"\nA mediana dos números na sequência é = {np.median(sequencia)}")

print(f"\nO desvio padrão dos números na sequência é = {sequencia.std()}")

print(f"\nA média aritmética dos números na sequência é = {sequencia.mean()}")

print(f"\nO valor máximo dos números na sequência é = {sequencia.max()}\nO valor mínimo dos números na sequência é = {sequencia.min()}")
```
