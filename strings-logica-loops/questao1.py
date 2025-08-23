## Descrição: Leia uma frase do usuário e mostre quantas vogais e consoantes há (ignore espaços, números e pontuação).  
# Exemplo: 
# Entrada: Programar é divertido! 
# Saída: Vogais: 8 | Consoantes: 10 
# Dica: use lower(), isalpha() e verifique se o caractere está em 'aeiou'. Um for sobre cada caractere ajuda.

vogais = []
consoantes = []

print("____Contar vogais e consoantes____")
frase = input("\nEscreva a frase para a análise: \n \n")
frase = frase.lower() # transforma tudo em minúsculo

for letras in frase: # verifica caractere por caractere da frase
    if letras.isalpha(): # se for letra
        if letras in("a", "e", "i", "o","u"): # verifica as vogais
            vogais.append(letras) # adiciona uma vogal na lista
        else:
            consoantes.append(letras) # o que não é vogal é adicionado na lista de consoantes

print("\nVogais:", len(vogais), "| Consoantes:", len(consoantes)) # len() faz a contagem de itens na lista

print("\nAs vogais são:", vogais)
print("As consoantes são:", consoantes, "\n")