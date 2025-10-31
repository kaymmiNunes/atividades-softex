from models.Transacao import Transacao
from datetime import datetime

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self, valor):
        return self._valor == valor

    def registrar(self, conta):
        if self._valor <= 0:
            return print("\n@@@ Valor de depósito inválido! @@@")

        conta.saldo += self._valor
        conta.historico.adicionar_transacao({
            'tipo': 'Depósito',
            'valor': self._valor,
            'data': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })
        
        return print(f"\n=== Depósito de R${self._valor:.2f} realizado com sucesso! Saldo atual: R${conta.saldo:.2f} ===")

