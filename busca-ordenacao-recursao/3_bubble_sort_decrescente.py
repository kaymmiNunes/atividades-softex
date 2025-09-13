valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista[::-1]

print(bubble_sort(valores))