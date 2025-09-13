# Desafio 🎯: Crie um programa que peça uma lista de números ao usuário e:
# Ordene a lista
# Pergunte um valor e faça a busca linear
# Mostre o fatorial desse número (se existir na lista)

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

numeros.sort()

print("Lista ordenada:", numeros)

busca = int(input("Digite um número para buscar na lista: "))

def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

resultado = busca_linear(numeros, busca)

if resultado != -1:
    print(f"Número {busca} encontrado na posição {resultado}.")
    print(f"O fatorial de {busca} é {fatorial(busca)}.")
else:
    print(f"Número {busca} não encontrado na lista.")

