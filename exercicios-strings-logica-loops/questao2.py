## Verificar palíndromo (ignorando espaços, maiúsculas e acentos)

import unicodedata  # para manipular caracteres especiais (remover acentos)

def remover_acentos(frase):
    return unicodedata.normalize('NFD', frase).encode('ascii', 'ignore').decode('utf-8')

print("____ Verificar palíndromo ____")
frase = input("\nEscreva a frase para a análise: ")

frase = remover_acentos(frase).lower().replace(" ", "")  # remove acentos, minúsculas e espaços
frase_invertida = frase[::-1]  # inverte a string

# Verifica se é palíndromo
if frase == frase_invertida:
    print(f"\nA frase - {frase} - é palíndromo\n")
else:
    print(f"\nA frase - {frase} - não é palíndromo\n")
