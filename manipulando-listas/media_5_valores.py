# Calcular média de 5 números

notas = []  # lista para armazenar as notas

for i in range(5):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

resultado = sum(notas) / len(notas)  # calcula a média
print("O resultado é:", resultado)
