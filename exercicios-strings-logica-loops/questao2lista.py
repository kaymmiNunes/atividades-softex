## Verificar palíndromo (ignorando espaços e maiúsculas) usando listas

letras = []  # letras da frase
contra = []  # letras invertidas

print("____ Verificar palíndromo ____")
frase = input("\nEscreva a frase para a análise: ").lower().replace(" ", "")

# Preenche a lista de letras
for letra in frase:
    if letra.isalpha():
        letras.append(letra)

# Cria a lista invertida
for letra in letras:
    contra.append(letra)

contra = contra[::-1]  # inverte a lista

# Verifica palíndromo
if letras == contra:
    print(f"\nA frase - {frase} - é palíndromo")
else:
    print(f"\nA frase - {frase} - não é palíndromo")

# Mostra listas
print("\nNormal:", letras)
print("Contrário:", contra, "\n")
