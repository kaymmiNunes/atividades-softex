# Verificar palíndromo (ignorando espaços e maiúsculas)
# Descrição: Leia uma palavra/frase e diga se é palíndromo (mesma leitura ao contrário), ignorando espaços e diferenças de maiúsculas/minúsculas.
# Exemplo:
# Entrada: Socorram me subino onibus em marrocos
# Saída: É palíndromo
# Dica: remova espaços com replace(" ", ""), aplique lower() e compare a string com ela invertida    s[::-1].

# Função criada para remover acentos
def remover_acentos(caractere):
    return unicodedata.normalize('NFD', caractere).encode('ascii', 'ignore').decode('utf-8')

print("____ Verificar palíndromo ____")
frase = input("\nEscreva a frase para a análise: ")
frase = frase.lower() # transforma tudo em minúsculo
frase = frase.replace(" ", "") # remove espaços
fraseContra = (frase[::-1]) # lê a string de trás pra frente (passo -1)

if frase in fraseContra:
    print(f"\nA frase - {frase} - é palíndromo\n")
else:
    print(f"\nA frase - {frase} - não é palíndromo\n")