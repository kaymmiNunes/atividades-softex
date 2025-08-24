notas = []  # lista para armazenar as notas digitadas pelo usuário

for i in range(5):  # loop que vai repetir 5 vezes
    nota = float(input("Digite as 5 notas para saber a média: "))  # entrada da nota e conversão para float
    i = i+1  # incrementa o contador (não necessário, mas presente)
    notas.append(nota)  # adiciona a nota na lista

resultado = (sum(notas) / len(notas))  # calcula a média somando as notas e dividindo pelo número de notas

print("O resultado é: ", resultado)  # exibe o resultado da média
