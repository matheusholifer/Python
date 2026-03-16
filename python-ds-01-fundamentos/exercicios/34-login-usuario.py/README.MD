38) Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja
diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a
mensagem ‘Usuário inválido!’. Caso o Código seja correto, deve ser lido outro valor que é a senha. Se
esta senha estiver incorreta (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’. Caso a
senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’.

```python
usuarios = [1234]
senhas = [9999]

usuario = int(input("\nInsira o número de usuário: "))
if usuario not in usuarios:
    print("\nUsuário inválido!")
else:
    senha = int(input("\nInsira a senha do usuário: "))
    if senha not in senhas:
        print("\nSenha incorreta.")
    else:
        print("\nAcesso permitido.")
```
