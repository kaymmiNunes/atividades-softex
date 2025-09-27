'''Implemente uma classe abstrata Veiculo com métodos abstratos acelerar e frear. 
Crie subclasses Carro e Moto.'''

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

class Carro(Veiculo):

    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, acelerar):
        self.velocidade += acelerar
        return print(f"O {self.modelo} está a {self.velocidade}")
    
    def frear(self, reduzir):
        self.velocidade -= reduzir
        return print(f"O {self.modelo} está a {self.velocidade}")
    
class Moto(Veiculo):

    def __init__(self, modelo):
        self.modelo = modelo 
        self.velocidade = 0
        
    def acelerar(self, acelerar):
        self.velocidade += acelerar
        return print(f"O {self.modelo} está a {self.velocidade}")
    
    def frear(self, reduzir):
        self.velocidade -= reduzir
        return print(f"O {self.modelo} está a {self.velocidade}")

civic = Carro("Civic")

civic.acelerar(10)
civic.acelerar(10)
civic.acelerar(10)
civic.frear(10)
civic.frear(10)
civic.frear(10)

cb250 = Moto("Cb Twister")

cb250.acelerar(10)
cb250.acelerar(20)
cb250.acelerar(20)
cb250.frear(10)
cb250.frear(10)
cb250.frear(10)







