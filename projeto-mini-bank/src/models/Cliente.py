class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if conta not in self.contas:
            return print("\n@@@ Esta conta não pertence a este cliente! @@@") 
        else:
            return transacao.registrar(conta)

    def adicionar_conta(self, conta):
        return self.contas.append(conta)
