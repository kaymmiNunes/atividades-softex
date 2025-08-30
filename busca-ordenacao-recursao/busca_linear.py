def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

numeros = [10, 23, 45, 70, 11, 15, 90, 34, 22]
print(busca_linear(numeros, 70))  # Saída: 3
print(busca_linear(numeros, 100)) # Saída: -1
print(busca_linear(numeros, 10))  # Saída: 0