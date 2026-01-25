1) Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B.
    A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o
    valor que está em A passe para B e vice-versa. Ao final, escrever os valores que ficaram armazenados
    nas variáveis.

### Forma 1:

```python
# Usando varíavel auxiliar
aux = a
a = b
b = aux
```

### Forma 2:

```python
# Usando operações básicas
a = a + b # A agora é 30
b = a - b # B agora é 10
a = a - b # A agora é 20
```

### Forma 3:

```python
# Usando operador bit a bit
a = a ^ b
b = a ^ b
a = a ^ b
```

- A forma três é mais eficiente na memória, mas requer que ambos variáveis tenham a mesma quantidade de bits. 
