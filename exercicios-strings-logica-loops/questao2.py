## Verificar palíndromo (ignorando espaços e maiúsculas)

import unicodedata  # importa a biblioteca usada para manipulação de caracteres especiais (acentos)

def remover_acentos(frase):  
    return unicodedata.normalize('NFD', frase).encode('ascii', 'ignore').decode('utf-8')  # normaliza e remove acentos

print("____ Verificar palíndromo ____")  # título do programa
frase = input("\nEscreva a frase para a análise: ")  # entrada da frase
frase = remover_acentos(frase)  # chama a função para remover acentos
frase = frase.lower()  # transforma tudo em minúsculo
frase = frase.replace(" ", "")  # remove espaços
fraseContra = (frase[::-1])  # inverte a string (lê de trás para frente, passo -1)

if frase in fraseContra:  # verifica se a frase normal é igual à invertida
    print(f"\nA frase - {frase} - é palíndromo\n")  # imprime se for palíndromo
else:
    print(f"\nA frase - {frase} - não é palíndromo\n")  # imprime se não for palíndromo
