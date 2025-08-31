# Verifica se a palavra é palíndromo e se é comum ou longa

import unicodedata  # para manipular caracteres Unicode (remover acentos)

# Remove acentos de uma palavra
def remover_acentos(palavra):
    return ''.join(
        c for c in unicodedata.normalize('NFD', palavra)
        if unicodedata.category(c) != 'Mn'
    )

ignorar = ["de", "da", "do", "das", "dos", "e"]  # palavras a serem ignoradas

frase = input("Escreva várias palavras (separadas por espaço): ")
palavras = frase.split()

# Contadores
inicio_Aa = 0
palindromo = 0
longa = 0
comum = 0

for palavra in palavras:
    palavra_limpa = remover_acentos(palavra.lower())

    if palavra_limpa in ignorar:
        continue

    condicoes = []

    if palavra_limpa[0] == "a":  
        condicoes.append("começa com A")
        inicio_Aa += 1

    if palavra_limpa == palavra_limpa[::-1]:
        condicoes.append("é palíndromo")
        palindromo += 1

    if len(palavra_limpa) >= 7:
        condicoes.append("é longa")
        longa += 1

    if not condicoes:
        condicoes.append("é comum")
        comum += 1

    print(f"{palavra}: {', '.join(condicoes)}")

# RESUMO FINAL
total_palavras = inicio_Aa + palindromo + longa + comum
print("\n====RESUMO====\n")
print(f"Palavras analisadas (não ignoradas): {total_palavras}")
print(f"Palavras que começam com A: {inicio_Aa}")
print(f"Palíndromos: {palindromo}")
print(f"Palavras longas: {longa}")
print(f"Palavras comuns: {comum}")
