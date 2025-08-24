## 

palavras = []

frase = input("Escreva várias palavras (separadas por espaço): ")  # entrada da frase
palavras = frase.split()  # separa a frase em palavras e cria uma lista

inicio_Aa = 0
palindromo = 0
longa = 0
comum = 0

for palavra in palavras:
    if palavra[0].upper() == "A":  # verifica se a primeira letra é A ou a
        print(f"{palavra} - começa com A")
        inicio_Aa = inicio_Aa + 1
    if palavra == palavra[::-1]:
        print(f"{palavra} - é palindromo")
        palindromo = palindromo + 1
    if len(palavra) >= 7:
        print(f"{palavra} - é longa")
        longa = longa + 1
    if len(palavra) < 7:
        print(f"{palavra} - é comum")
        comum = comum + 1

# RESUMO:
print("\n====RESUMO====\n")
print(f"Palavras que começam com A: {inicio_Aa}")
print(f"Palíndromos: {palindromo}")
print(f"Palavras longas: {longa}")
print(f"Palavras comuns: {comum}")