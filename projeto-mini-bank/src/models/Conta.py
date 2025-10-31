from models.Historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        self.saldo =- valor
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return print(f"\n=== Depósito de R${valor} realizado com sucesso! ===")
        else:
            return print("\n@@@ Operação falhou! O valor informado é inválido. @@@") 