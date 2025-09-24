'''Crie as classes Cliente e ContaBancaria.
O cliente tem nome e CPF.
A conta bancária tem número e um cliente associado.
Imprima uma mensagem mostrando o titular da conta e o número da conta.'''

class Cliente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        

class ContaBancaria:

    def __init__(self, numero, cliente: Cliente):
        self.numero = numero
        self.cliente = cliente

    def adicionar_cliente(self):
        return self.cliente
    
    def mostrar_clientes(self):
            print(f"Cliente: {self.cliente.nome} - CPF: {self.cliente.cpf} - Conta: {self.numero}")

cliente1 = Cliente("Kaymmi", "111.222.333-44")
conta1 = ContaBancaria("1234-5", cliente1)

conta1.mostrar_clientes()