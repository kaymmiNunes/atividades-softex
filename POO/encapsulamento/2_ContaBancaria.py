class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular # Atributo público
        self.__saldo = saldo # Atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return self.__saldo
        else:
            return "Valor de depósito inválido" 

    def sacar(self, valor):
        if self.__saldo >= valor:
             self.__saldo -= valor
             return self.__saldo
        else:
            return "Saldo insuficiente" 
            
    def ver_saldo(self):
        return self.__saldo
    
conta = ContaBancaria("Kaymmi", 1000)

print(conta.ver_saldo())
print(conta.depositar(500))
print(conta.sacar(2000))