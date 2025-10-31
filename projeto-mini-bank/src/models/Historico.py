from datetime import datetime

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """Adiciona uma transação ao histórico"""
        self._transacoes.append(transacao)

    def mostrar_extrato(self):
        """Exibe todas as transações do histórico"""
        if not self._transacoes:
            print("\nNão foram realizadas movimentações.")
            return

        print("\n================ EXTRATO ================")
        for t in self._transacoes:
            print(f"{t['tipo']}:\n\tR$ {t['valor']:.2f}\n\tData: {t['data']}")
        print("==========================================")