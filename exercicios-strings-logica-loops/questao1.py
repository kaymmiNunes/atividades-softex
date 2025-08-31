## Identificar vogais e consoantes

import unicodedata  # para remover acentos

def remover_acentos(frase):
    return unicodedata.normalize('NFD', frase).encode('ascii', 'ignore').decode('utf-8')

vogais = []       # lista para armazenar vogais
consoantes = []   # lista para armazenar consoantes

print("____Contar vogais e consoantes____")

frase = input("\nEscreva a frase para a análise: \n \n")
frase = remover_acentos(frase.lower())  # minúsculas e sem acentos

for letra in frase:
    if letra.isalpha():  # ignora espaços, números e pontuação
        if letra in "aeiou":
            vogais.append(letra)
        else:
            consoantes.append(letra)

# Resultado
print("\nVogais:", len(vogais), "| Consoantes:", len(consoantes))
print("\nAs vogais são:", vogais)
print("As consoantes são:", consoantes, "\n")
