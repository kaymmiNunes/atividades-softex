'''Exercício 2: Classe Abstrata Básica
Crie uma classe abstrata chamada FormaGeometrica usando o módulo abc. Esta classe
deve ter um método abstrato chamado calcular_area(). Crie uma classe concreta
Retangulo que herda de FormaGeometrica. A classe Retangulo deve ter atributos para
largura e altura e implementar o método calcular_area() para retornar a área correta.'''

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

retangulo = Retangulo(5, 10)

print(f'Área do Retângulo: {retangulo.calcular_area()}')

