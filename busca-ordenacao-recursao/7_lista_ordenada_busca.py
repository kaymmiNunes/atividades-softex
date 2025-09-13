# Crie um programa que pergunte ao usuário 5 números, salve em uma lista e:
    # Mostre a lista ordenada (usando sort() e sorted())
    # Procure um número escolhido pelo usuário na lista usando busca linear

numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("Lista ordenada usando sort():")
numeros.sort()
print(numeros)
print("Lista ordenada usando sorted():")
print(sorted(numeros))
busca = int(input("Digite um número para buscar na lista: "))
def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

resultado = busca_linear(numeros, busca)
if resultado != -1:
    print(f"Número {busca} encontrado na posição {resultado}.")
else:
    print(f"Número {busca} não encontrado na lista.")