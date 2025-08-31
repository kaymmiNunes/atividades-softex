# Somar 10 números, retirar o último e calcular o total até a lista ficar vazia

valores = []  # lista para armazenar os valores

# Entrada de 10 valores
for i in range(10):
    valor = float(input("Digite o valor: "))
    valores.append(valor)
    print(f"Valor total até agora: {sum(valores)}")

print("O valor total final é: ", sum(valores))

# Remoção dos valores (um por vez)
for i in range(10):
    valores.pop()
    print(f"Removendo o último, temos: {sum(valores)}")
