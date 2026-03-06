31) Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam
ou não um triângulo. OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma
dos outros 2 lados

```python
# Coleta de Dados
a, b, c = map(float, input("\nInsira os três lados de um triângulo, sepradaos por vírgula e espaço: ").split(', '))

# Função para Verificacar se forma um triângulo
verificar_triangulo = lambda a, b, c: (a + b > c) and (a + c > b) and (b + c > a)
status = verificar_triangulo(a, b, c)

# Imprime relátório
if status == True:
    print(f"\nOs lados {a=}, {b=}, {c=}, formam um triângulo!")
else:
    print(f"\nOs lados {a=}, {b=}, {c=}, não formam um triângulo.")
```
