#1. Listas: Crie uma lista com os números de 1 a 5 e imprima cada elemento.
print("\n1. Listas: Crie uma lista com os números de 1 a 5 e imprima cada elemento.\n")

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

#2. Condicionais: Peça um número ao usuário e verifique se é positivo, negativo ou zero.
print("\n2. Condicionais: Peça um número ao usuário e verifique se é positivo, negativo ou zero.\n")
try:
    numero = float(input("Digite um número: "))
    if numero >= 0:
        print(f"O número {numero} é positivo.")
    else: 
        print(f"O número {numero} é negativo.")
except:
    print("Provavelmente você escreveu uma letra ou símbolo. \
          Rode o programa novamente e digite um número.")

#3. Laços: Use um loop for para imprimir os números de 1 a 10.
print("\n3. Laços: Use um loop for para imprimir os números de 1 a 10.\n")

for i in range(1, 11):
    print(i)

#4. Dicionários: Crie um dicionário com nomes e idades de 3 pessoas e imprima cada par.
print("\n4. Dicionários: Crie um dicionário com nomes e idades de 3 pessoas e imprima cada par.\n")

pessoas = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35
}

for nome, idade in pessoas.items():
    print(f"{nome} tem {idade} anos.")

#5. Funções: Crie uma função que recebe dois números e retorna a soma.
print("\n5. Funções: Crie uma função que recebe dois números e retorna a soma.\n")

def soma(a, b):
    return a + b

numero1 = float(input("Digite o primeiro número: ")) 
numero2 = float(input("Digite o segundo número: "))
resultado = soma(numero1, numero2)
print(f"A soma de {numero1} e {numero2} é {resultado}.")

#6. Strings: Peça uma palavra ao usuário e imprima o número de caracteres.
print("\n6. Strings: Peça uma palavra ao usuário e imprima o número de caracteres.\n")

letras = []
palavra = input("Digite uma palavra: ")
for letra in palavra:
    letras.append(letra)
    quantidade = len(letras)

print(f"A palavra '{palavra}' tem {quantidade} letras.")
