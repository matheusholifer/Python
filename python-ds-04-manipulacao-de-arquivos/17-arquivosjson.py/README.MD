Um código introsutório a arquivos JSON em Python.

```python
# Escrevendo JSON
import json

configuracoes = {
    "personagem": "Nicolau Copérnico",
    "civilizacao": "Era de Aristóteles / Modelo Geocêntrico",
    "status": "Desidratado",
    "inventario": [
        "Relógio de sol",
        "Pergaminhos de observação",
        "Ampulheta"
    ],
    "preferencias": {
        "modelo_cosmologico": "Heliocêntrico",
        "previsao_climatica": "Era Estável"
    },
    "objetivo": "Determinar a estrutura do universo para evitar a reidratação em chamas"
}

with open('config.json', 'w', encoding='utf-8') as arquivo_json:
    # indent=4 deixa o arquivo formatado e bonito
    # ensure_ascii=False permite acentos corretos no arquivo final
    json.dump(configuracoes, arquivo_json, indent=4, ensure_ascii=False)

# Lendo JSON
with open('config.json', 'r', encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)

print(f"Bem-vindo de volta, {dados['personagem']}!")
print(f"Seu inventário: {dados['inventario']}")
```
