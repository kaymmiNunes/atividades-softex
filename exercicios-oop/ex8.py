'''Exercício 8: Abstração e Herança para Sistema de Cadastro
Crie um sistema de cadastro com classes abstratas e herança:
1. Classe Abstrata Pessoa com atributos id e nome e um método abstrato
detalhes_de_cadastro().
2. Classe Concreta Cliente que herda de Pessoa e adiciona o atributo data_cadastro.
Implemente detalhes_de_cadastro().
3. Classe Concreta Fornecedor que herda de Pessoa e adiciona o atributo cnpj.
Implemente detalhes_de_cadastro().
4. Crie uma função que aceita uma lista de objetos que são Pessoa (ou seja,
instâncias de Cliente ou Fornecedor) e itere sobre ela, chamando o método
detalhes_de_cadastro() para cada item.'''

from abc import ABC, abstractmethod

class Pessoa(ABC):

    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

    @abstractmethod
    def detalhes_de_cadastro(self):
        pass

class Cliente(Pessoa):

    def __init__(self, nome, id, data_cadastro):
        super().__init__(nome, id)
        self.data_cadastro = data_cadastro

    def detalhes_de_cadastro(self):
        print(f"Cliente:\nNome: {self.nome} \nID: {self.id} \nData de cadastro: {self.data_cadastro}\n")

class Fornecedor(Pessoa):

    def __init__(self, nome, id, cnpj):
        super().__init__(nome, id)
        self.cnpj = cnpj
    
    def detalhes_de_cadastro(self):
        print(f"Fornecedor:\nNome: {self.nome} \nID: {self.id} \nCNPJ: {self.cnpj}\n")

def mostrar_cadastros(lista_pessoas):
    for pessoa in lista_pessoas:
        pessoa.detalhes_de_cadastro()

pessoas = [
    Cliente("André", 1, "01/01/2020"),  
    Fornecedor("Empresa X", 2, "12.345.678/0001-99"),
    Cliente("Maria", 3, "22/07/2021"),
    Fornecedor("Empresa Y", 4, "98.765.432/0001-55")
]

mostrar_cadastros(pessoas)
