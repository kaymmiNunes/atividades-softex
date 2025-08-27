# Somar 10 números, retirar o último e calcular o total até acabar a lista 

valores = []  # lista para armazenar os valores digitados

for i in range(10):  # Loop para adicionar 10 valores
    valor = float(input("Digite o valor: "))  # recebe o valor do usuário e converte para float
    valores.append(valor)  # adiciona o valor à lista
    valor_total = sum(valores)  # calcula a soma total da lista após cada entrada
    print(f"Valor total até agora: {valor_total}")  # imprime o valor total atualizado

print("O valor total final é: ", sum(valores))  # imprime a soma final de todos os valores

for i in range(10):  # Loop para remover os valores da lista
    valores.pop()  # remove o último valor da lista
    valor_total = sum(valores)  # recalcula o valor total após cada remoção
    print(f"Removendo o último, temos: {valor_total}")  # imprime o valor total atualizado após remoção
