## Gerar acrônimo a partir de uma frase

ignorar = ["de", "da", "do", "das", "dos", "e"]  # palavras a ignorar
palavras_sem_comuns = []  # palavras importantes

frase = input("\nEscreva a frase para gerar acrônimo: ")
palavras = frase.split()  # separa a frase em palavras

# Filtra palavras importantes
for palavra in palavras:
    if palavra not in ignorar:
        palavras_sem_comuns.append(palavra)

# Gera acrônimo com a primeira letra de cada palavra
sigla = ".".join(p[0].upper() for p in palavras_sem_comuns)
print(sigla)
