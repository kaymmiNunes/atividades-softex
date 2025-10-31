from models.Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_realizados = 0

    def sacar(self, valor):
        if self._saques_realizados >= self._limite_saques:
            return print("\n@@@ Limite diário de saques atingido! @@@")
        if valor > self._limite:
            return print(f"\n@@@ Valor excede o limite por saque (R${self._limite:.2f})! @@@")

        # Chama o método da classe base Conta
        sucesso = super().sacar(valor)
        if sucesso:
            self._saques_realizados += 1
        return sucesso

    def __str__(self):
        return f"""\ 
Agência:\t{self.agencia}
C/C:\t\t{self.numero}
Titular:\t{self.cliente.nome}
"""
