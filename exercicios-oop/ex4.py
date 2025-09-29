'''Exercício 4: Abstração com Propriedades
Crie uma classe abstrata Veiculo. Ela deve ter um método abstrato acelerar() e uma
propriedade abstrata (usando @abstractmethod e @property) chamada rodas que as
classes filhas devem implementar. Crie duas classes filhas: Carro (rodas = 4) e Moto (rodas
= 2). Ambas devem implementar acelerar() com uma mensagem relevante.'''

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self, incremento):
        pass

    @property
    @abstractmethod
    def rodas(self):
        pass

class Carro(Veiculo):
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0
        self._rodas = 4

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O {self.modelo} está a {self.velocidade} km/h")

    @property
    def rodas(self):
        return self._rodas

class Moto(Veiculo):
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0
        self._rodas = 2

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"A {self.modelo} está a {self.velocidade} km/h")

    @property
    def rodas(self):
        return self._rodas

civic = Carro("Civic")
civic.acelerar(10)
civic.acelerar(10)
print(f"O {civic.modelo} tem {civic.rodas} rodas\n")

cb250 = Moto("CB Twister")
cb250.acelerar(15)
cb250.acelerar(15)
print(f"A {cb250.modelo} tem {cb250.rodas} rodas")
