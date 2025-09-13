# Escreva uma função recursiva que conte quantos elementos existem em uma lista.

def conta_elementos(lista):
    if not lista:
        return 0
    else:
        return 1 + conta_elementos(lista[1:])  
    
print(conta_elementos([1, 2, 3, 4, 5]))  # Saída: 5
print(conta_elementos([]))  # Saída: 0