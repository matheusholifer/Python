8) Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
    brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total
    de eleitores.

```python
# Coleta de dados
total_eleitores, votos_brancos, votos_nulos, votos_validos = map(float, input("\nInsira o total de eleitores, o número de votos brancos, o número de votos nulos e o número de votos válidos. Separe por vírgula: ").split(', '))

# Cálculo da porcentagem
parcela_brancos = (votos_brancos / total_eleitores) * 100
parcela_nulos = (votos_nulos / total_eleitores) * 100
parcela_validos = (votos_validos / total_eleitores) * 100

# Imprime o relátorio
print(f"\nTotal de eleitores: {total_eleitores}\n\n\tVotos brancos: {votos_brancos} = {parcela_brancos}%\n\tVotos nulos: {votos_nulos} = {parcela_nulos}%\n\tVotos válidos: {votos_validos} = {parcela_validos}%")
```
