# Calcular a média de números digitados (sem limite de quantidade)

notas = []  # lista para armazenar os valores

while True:
    entrada = input("Digite um valor (ou Enter para sair): ")
    if entrada == "":  # encerra quando nada for digitado
        break
    notas.append(float(entrada))  # converte e adiciona à lista

resultado = sum(notas) / len(notas)  # calcula a média
print("O resultado é:", resultado)
