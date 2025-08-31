# Busca linear para contar ocorrências de um valor em uma lista

lista = [10, 23, 45, 10, 11, 15, 90, 10, 22]

def contar_ocorrencias(lista, valor):
    contar = 0
    for i in range(len(lista)):
        if lista[i] == valor: 
            contar += 1
    return contar

print(contar_ocorrencias(lista, 10))
# or
def usar_count(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor: 
            return lista.count(valor)

print(usar_count(lista, 10))