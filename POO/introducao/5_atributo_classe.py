class ContaBancaria:
    
    banco = "Banco Central" # Atributo de classe

    def __init__(self, titular, saldo): # Método construtor
        self.titular = titular # Atributo de instância
        self.saldo = saldo # Atributo de instância

    def mostrar_objetos(self): # Método de instância
        return f"Banco: {self.banco}  Titular: {self.titular}  Saldo: {self.saldo}"

pessoa1 = ContaBancaria("Antonio", 1000)
pessoa2 = ContaBancaria("Carlos", 2000)

print(pessoa1.mostrar_objetos())
print(pessoa2.mostrar_objetos())


