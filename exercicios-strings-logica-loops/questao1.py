## Identificar vogais e consoantes

import unicodedata   # importa a biblioteca usada para remover acentos das letras

def remover_acentos(frase): # função que remove acentuação de uma frase ou palavra
    return unicodedata.normalize('NFD', frase).encode('ascii', 'ignore').decode('utf-8')

vogais = []       # cria uma lista vazia para armazenar todas as vogais encontradas
consoantes = []   # cria uma lista vazia para armazenar todas as consoantes encontradas

print("____Contar vogais e consoantes____")   # título inicial para o usuário

frase = input("\nEscreva a frase para a análise: \n \n") # recebe uma frase do usuário

frase = frase.lower()           # transforma todos os caracteres em minúsculo
frase = remover_acentos(frase)  # chama a função para remover acentos da frase

for letras in frase:  # percorre letra por letra dentro da frase
    if letras.isalpha():   # verifica se o caractere é uma letra (ignora espaço, número, pontuação)
        if letras in ("a", "e", "i", "o", "u"):   # se a letra for uma vogal
            vogais.append(letras)      # adiciona a letra na lista de vogais
        else:  
            consoantes.append(letras)  # se não for vogal, adiciona na lista de consoantes

# mostra quantas vogais e consoantes foram encontradas (len() conta os itens de cada lista)
print("\nVogais:", len(vogais), "| Consoantes:", len(consoantes))  

# mostra a lista com todas as vogais encontradas
print("\nAs vogais são:", vogais)

# mostra a lista com todas as consoantes encontradas
print("As consoantes são:", consoantes, "\n")
