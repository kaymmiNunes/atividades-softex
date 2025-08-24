notas = []  # lista para armazenar as notas digitadas pelo usuário

while True:  # loop infinito que só termina quando o usuário não digitar nada
    entrada = input("Digite os valores para clacular a média: ")  # recebe a entrada como string
    if entrada == "":  # verifica se o usuário não digitou nada
        break  # sai do loop se a entrada for vazia
    else: 
        entrada = float(entrada)  # converte a entrada de string para float
        notas.append(entrada)  # adiciona a nota na lista

resultado = float(sum(notas) / len(notas))  # calcula a média das notas convertendo para float
print("O resultado é: ", resultado)  # exibe o resultado da média
