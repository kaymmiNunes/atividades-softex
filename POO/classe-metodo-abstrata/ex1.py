'''Crie uma classe abstrata Funcionario com um método abstrato calcular_bonus. 
Crie subclasses Gerente e Desenvolvedor que implementem regras diferentes de bônus.'''

from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcular_bonus(self):
        pass

class Gerente(Funcionario):
    def __init__(self, salario):
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.2
    
class Desenvolvedor(Funcionario):
    def __init__(self, salario):
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.1
    
gerente = Gerente(5000)
desenvolvedor = Desenvolvedor(4000)

print(f'Bônus do Gerente: R$ {gerente.calcular_bonus():.2f}')
print(f'Bônus do Desenvolvedor: R$ {desenvolvedor.calcular_bonus():.2f}')


