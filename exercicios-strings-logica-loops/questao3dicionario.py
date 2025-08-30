## Frequência de palavras

import unicodedata  # biblioteca usada para manipular caracteres especiais

def remover_acentos(frase):  
    return unicodedata.normalize('NFD', frase).encode('ascii', 'ignore').decode('utf-8')  # normaliza e remove acentos

frase = input("Escreva a frase para a análise: ")  # entrada da frase

frase = remover_acentos(frase.lower())  # deixa tudo em minúsculo e sem acento

palavras = frase.split()  # separa a frase em palavras e cria uma lista

frequencia = {}  # dicionário para armazenar a frequência de cada palavra

for palavra in palavras:  # percorre cada palavra da lista
    if palavra in frequencia:  # verifica se a palavra já existe no dicionário
        frequencia[palavra] += 1  # se existir, soma +1
    else:
        frequencia[palavra] = 1  # se não existir, adiciona com valor 1

for palavra, contagem in frequencia.items():  # percorre as chaves e valores do dicionário
    print(f"{palavra}: {contagem}")  # imprime a palavra e a quantidade que apareceu
