'''Exercício 6: Classe Abstrata com Método Concreto
Crie uma classe abstrata ContaBancaria. Ela deve ter um método abstrato sacar(valor) e
um método concreto chamado verificar_saldo() que usa um atributo saldo (inicializado no
construtor) para imprimir o saldo atual. Crie uma classe filha ContaCorrente que
implementa o método sacar(valor) (simplesmente subtrai o valor do saldo). Crie uma lista de
objetos ContaCorrente e itere sobre ela chamando sacar e verificar_saldo.'''

from abc import ABC, abstractmethod

class ContaBancaria(ABC):

    def __init__(self, saldo):
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor):
        pass

    def verificar_saldo(self):
        return print(f"O saldo atual é R${self.saldo}")
    
class ContaCorrente(ContaBancaria):

    def __init__(self, saldo, nome, conta):
        super().__init__(saldo)
        self.nome = nome
        self.conta = conta

    def sacar(self, valor):
        self.valor = valor
        self.saldo -= self.valor
        return print(f"Foi sacado da conta corrente de {self.nome} ({self.conta}): R${self.valor} \nValor restante: R${self.saldo} ")

contas = [
    ContaCorrente(1000, "André", "123-4"),
    ContaCorrente(500, "Maria", "567-8"),
    ContaCorrente(2000, "João", "910-1")
]

for conta in contas:
    print("-----")
    conta.sacar(100)
    conta.verificar_saldo()

print("-----")
