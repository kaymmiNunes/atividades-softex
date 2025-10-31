from models.Transacao import Transacao
from datetime import datetime

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        """Aplica o saque na conta e registra no histórico"""
        if self._valor <= 0:
            print("\n@@@ Valor de saque inválido! @@@")
            return False
        if self._valor > conta.saldo:
            print("\n@@@ Saldo insuficiente! @@@")
            return False

        conta.saldo -= self._valor
        conta.historico.adicionar_transacao({
            'tipo': 'Saque',
            'valor': self._valor,
            'data': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })
        print(f"\n=== Saque de R${self._valor:.2f} realizado com sucesso! Saldo atual: R${conta.saldo:.2f} ===")
        return True
