## Frequência de palavras em uma frase

import unicodedata  # para remover acentos

def remover_acentos(frase):
    return unicodedata.normalize('NFD', frase).encode('ascii', 'ignore').decode('utf-8')

frase = input("Escreva a frase para a análise: ")
frase = remover_acentos(frase.lower())  # minúsculas e sem acentos

palavras = frase.split()  # cria lista de palavras
frequencia = {}  # dicionário para contar palavras

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

# Mostra a frequência de cada palavra
for palavra, contagem in frequencia.items():
    print(f"{palavra}: {contagem}")
