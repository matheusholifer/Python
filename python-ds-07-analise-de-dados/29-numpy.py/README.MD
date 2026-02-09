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
