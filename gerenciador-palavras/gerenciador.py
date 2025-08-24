import unicodedata  # importa biblioteca para manipulação de caracteres Unicode

# Função para remover acentos
def remover_acentos(palavra):
    return ''.join(
        c for c in unicodedata.normalize('NFD', palavra)
        if unicodedata.category(c) != 'Mn'
    )

ignorar = ["de", "da", "do", "das", "dos", "e"]  # palavras pequenas para ignorar

frase = input("Escreva várias palavras (separadas por espaço): ")  # entrada do usuário
palavras = frase.split()  # separa a frase em lista de palavras

inicio_Aa = 0
palindromo = 0
longa = 0
comum = 0

for palavra in palavras:
    palavra_limpa = remover_acentos(palavra.lower())  # minúsculo e sem acento

    if palavra_limpa in ignorar:  # ignora palavras pequenas
        continue

    condicoes = []

    if palavra_limpa[0] == "a":  # começa com A
        condicoes.append("começa com A")
        inicio_Aa += 1

    if palavra_limpa == palavra_limpa[::-1]:  # palíndromo
        condicoes.append("é palíndromo")
        palindromo += 1

    if len(palavra_limpa) >= 7:  # longa
        condicoes.append("é longa")
        longa += 1

    if not condicoes:  # nenhuma condição anterior
        condicoes.append("é comum")
        comum += 1

    print(f"{palavra}: {', '.join(condicoes)}")

# RESUMO FINAL
total_palavras = inicio_Aa + palindromo + longa + comum  # total de palavras analisadas
print("\n====RESUMO====\n")
print(f"Palavras analisadas (não ignoradas): {total_palavras}")
print(f"Palavras que começam com A: {inicio_Aa}")
print(f"Palíndromos: {palindromo}")
print(f"Palavras longas: {longa}")
print(f"Palavras comuns: {comum}")
