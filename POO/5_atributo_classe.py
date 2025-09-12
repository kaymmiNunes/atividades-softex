class ContaBancaria:
    banco = "Banco Central"

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_objetos(self):
        return f"Banco: {self.banco}  Titular: {self.titular}  Saldo: {self.saldo}"

pessoa1 = ContaBancaria("Antonio", 1000)
pessoa2 = ContaBancaria("Carlos", 2000)


print(pessoa1.mostrar_objetos())
print(pessoa2.mostrar_objetos())

