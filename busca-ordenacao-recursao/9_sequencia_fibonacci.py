# Implemente a sequência de Fibonacci de forma iterativa e compare com a recursiva.

def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

n = 10
print(f"Fibonacci iterativo de {n}: {fibonacci_iterativo(n)}")
print(f"Fibonacci recursivo de {n}: {fibonacci_recursivo(n)}")