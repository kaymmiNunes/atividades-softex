# Verificar se a palavra é palindromo e se é comum ou longa

import unicodedata  # importa a biblioteca para manipulação de caracteres Unicode (acentos)

# Função para remover acentos de uma palavra
def remover_acentos(palavra):
    return ''.join(  # junta novamente os caracteres sem acentos
        c for c in unicodedata.normalize('NFD', palavra)  # separa letras e acentos
        if unicodedata.category(c) != 'Mn'  # ignora os caracteres de marca (acentos)
    )

ignorar = ["de", "da", "do", "das", "dos", "e"]  # palavras pequenas a serem ignoradas

frase = input("Escreva várias palavras (separadas por espaço): ")  # entrada do usuário
palavras = frase.split()  # separa a frase em uma lista de palavras

inicio_Aa = 0  # contador de palavras que começam com A
palindromo = 0  # contador de palíndromos
longa = 0  # contador de palavras longas (>= 7 caracteres)
comum = 0  # contador de palavras comuns

for palavra in palavras:  # percorre cada palavra da lista
    palavra_limpa = remover_acentos(palavra.lower())  # minúsculo e sem acentos

    if palavra_limpa in ignorar:  # verifica se a palavra está na lista de ignoradas
        continue  # pula a palavra se for para ignorar

    condicoes = []  # lista que vai armazenar as condições que se aplicam à palavra

    if palavra_limpa[0] == "a":  # verifica se começa com A
        condicoes.append("começa com A")  # adiciona condição à lista
        inicio_Aa += 1  # incrementa contador de palavras que começam com A

    if palavra_limpa == palavra_limpa[::-1]:  # verifica se é palíndromo
        condicoes.append("é palíndromo")  # adiciona condição à lista
        palindromo += 1  # incrementa contador de palíndromos

    if len(palavra_limpa) >= 7:  # verifica se é longa
        condicoes.append("é longa")  # adiciona condição à lista
        longa += 1  # incrementa contador de palavras longas

    if not condicoes:  # se nenhuma das condições acima se aplicou
        condicoes.append("é comum")  # adiciona "é comum" à lista
        comum += 1  # incrementa contador de palavras comuns

    print(f"{palavra}: {', '.join(condicoes)}")  # mostra a palavra e as condições aplicáveis

# RESUMO FINAL
total_palavras = inicio_Aa + palindromo + longa + comum  # total de palavras analisadas (não ignoradas)
print("\n====RESUMO====\n")  # título do resumo
print(f"Palavras analisadas (não ignoradas): {total_palavras}")  # mostra total de palavras
print(f"Palavras que começam com A: {inicio_Aa}")  # mostra total de palavras que começam com A
print(f"Palíndromos: {palindromo}")  # mostra total de palíndromos
print(f"Palavras longas: {longa}")  # mostra total de palavras longas
print(f"Palavras comuns: {comum}")  # mostra total de palavras comuns
