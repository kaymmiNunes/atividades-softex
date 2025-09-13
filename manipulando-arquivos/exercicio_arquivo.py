import random

# 1. Gerar arquivo com 200 clientes

total_dividas = 0

with open("manipulando-arquivos/clientes.txt", "w") as arquivo:
    for i in range(1, 201):
        nome = f"Cliente{i}"
        saldo = random.randint(500, 5000)   # saldo entre 500 e 5000
        divida = random.randint(100, 6000)  # dívida entre 100 e 6000
        arquivo.write(f"{nome},{saldo},{divida}\n")
        total_dividas += divida

print("Arquivo clientes.txt gerado com sucesso!")


# 2. Ler arquivo e atualizar saldos
clientes_atualizados = []
sem_divida = 0
com_divida = 0

with open("manipulando-arquivos/clientes.txt", "r") as arquivo:
    for linha in arquivo:
        nome, saldo, divida = linha.strip().split(",")
        saldo = int(saldo)
        divida = int(divida)

        # Comparar saldo e dívida
        if saldo >= divida:
            saldo -= divida   # paga toda a dívida
            divida = 0
            sem_divida += 1
        else:
            divida -= saldo   # reduz a dívida pelo saldo disponível
            saldo = 0
            com_divida += 1

        clientes_atualizados.append((nome, saldo, divida))


# 3. Salvar resultados em outro arquivo
with open("manipulando-arquivos/clientes_atualizados.txt", "w") as arquivo:
    divida_atual = 0
    arquivo.write("Nome,Saldo Atual,Divida Atual\n")
    for nome, saldo, divida in clientes_atualizados:
        arquivo.write(f"{nome},{saldo},{divida}\n")
        divida_atual += divida

print("Arquivo clientes_atualizados.txt criado com os saldos atualizados!")

print("Estatisticas:")

#Total de dividas antes do processamento
print("Total de dívidas geradas: R$ {:,.2f}".format(total_dividas).replace(",", "X").replace(".", ",").replace("X", "."))
#Clientes sem dívida
print(f"Clientes sem dívida: {sem_divida}")
#Clientes com dívida
print(f"Clientes com dívida: {com_divida}")
#Total de dívidas atuais
print("Total de dívidas atuais: R$ {:,.2f}".format(divida_atual).replace(",", "X").replace(".", ",").replace("X", "."))
