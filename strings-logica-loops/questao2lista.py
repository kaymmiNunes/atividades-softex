# Verificar palíndromo (ignorando espaços e maiúsculas)
# Descrição: Leia uma palavra/frase e diga se é palíndromo (mesma leitura ao contrário), ignorando espaços e diferenças de maiúsculas/minúsculas.
# Exemplo:
# Entrada: Socorram me subino onibus em marrocos
# Saída: É palíndromo
# Dica: remova espaços com replace(" ", ""), aplique lower() e compare a string com ela invertida    s[::-1].

letras = []
contra = []

print("____ Verificar palíndromo ____")
frase = input("\nEscreva a frase para a análise: ")
frase = frase.lower() # transforma tudo em minúsculo
frase = frase.replace(" ", "") # remove espaços

for letra in frase: # verifica caractere por caractere da frase
    if letra.isalpha(): # se for letra (ignorando outros caracteres)
        letras.append(letra) # adiciona as letras na lista

for letra in letras: # verifica caractere por caractere da lista
    if letra.isalpha(): # se for letra (ignorando outros caracteres)
        contra.append(letra) # adiciona as letras na lista

contra = contra[::-1]

if letras == contra: # lê a string de trás pra frente (passo -1)
    print(f"\nA frase - {frase} - é palíndromo")
else:
    print(f"\nA frase - {frase} - não é palíndromo")

print("\nNormal: ", letras)
print("\nContrário: ", contra, "\n")