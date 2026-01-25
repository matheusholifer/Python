6) Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo.

```python
area_retangulo = lambda b, h: b * h

b, h = map(int, input("\nInsira a base e a altura do retângulo em cm: "))
print(f"\n\tA área do retâangulo é: {area_retangulo(b,h)}cm²")
```
