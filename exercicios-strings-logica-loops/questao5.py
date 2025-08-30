## Gerar acrônimo

palavras = []  # lista para armazenar todas as palavras da frase
ignorar = ["de", "da", "do", "das", "dos", "e"]  # lista de palavras que serão ignoradas
palavras_sem_comuns = []  # lista para armazenar palavras importantes (sem as palavras ignoradas)

frase = input("\nEscreva a frase para gerar acrônimo: ")  # entrada da frase
palavras = frase.split()  # separa a frase em palavras e adiciona na lista

for palavra in palavras:  # percorre cada palavra da lista
    if palavra in ignorar:  # verifica se a palavra está na lista de ignoradas
        continue  # pula essa palavra
    else:
        palavras_sem_comuns.append(palavra)  # adiciona a palavra na lista de palavras importantes

# pega a primeira letra de cada palavra, transforma em maiúscula e junta com ponto
sigla = ".".join(p[0].upper() for p in palavras_sem_comuns)  

print(sigla)

