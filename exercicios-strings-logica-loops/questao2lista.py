## Verificar palíndromo (ignorando espaços e maiúsculas) com lista

letras = []  # lista que vai armazenar as letras normais
contra = []  # lista que vai armazenar as letras invertidas

print("____ Verificar palíndromo ____")  # título do programa
frase = input("\nEscreva a frase para a análise: ")  # entrada da frase
frase = frase.lower()  # transforma tudo em minúsculo
frase = frase.replace(" ", "")  # remove espaços

for letra in frase:  # percorre caractere por caractere da frase
    if letra.isalpha():  # verifica se é letra (ignora números e símbolos)
        letras.append(letra)  # adiciona a letra na lista de letras

for letra in letras:  # percorre caractere por caractere da lista de letras
    if letra.isalpha():  # verifica se é letra (mesma checagem anterior)
        contra.append(letra)  # adiciona a letra na lista contra

contra = contra[::-1]  # inverte a lista (lê de trás para frente)

if letras == contra:  # compara a lista normal com a lista invertida
    print(f"\nA frase - {frase} - é palíndromo")  # imprime se for palíndromo
else:
    print(f"\nA frase - {frase} - não é palíndromo")  # imprime se não for palíndromo

print("\nNormal: ", letras)  # mostra a lista normal
print("\nContrário: ", contra, "\n")  # mostra a lista invertida
