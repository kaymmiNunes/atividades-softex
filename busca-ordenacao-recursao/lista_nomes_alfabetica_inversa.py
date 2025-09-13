# Lista de nomes em ordem alfabética inversa

nomes = ["Ana", "Carlos", "Beatriz", "Daniel", "Eva"]

def inverter_nomes(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista[::-1]

print(inverter_nomes(nomes)) 