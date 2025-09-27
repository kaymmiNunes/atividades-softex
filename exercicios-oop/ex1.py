'''Exercício 1: Herança Simples de Atributos e Métodos
Crie uma classe base chamada Animal com um construtor que aceita o atributo nome. Ela
deve ter um método chamado emitir_som() que apenas imprime "Som genérico". Em
seguida, crie uma classe Cachorro que herda de Animal. No Cachorro, sobrescreva
(override) o método emitir_som() para imprimir "Latido!". Crie instâncias de ambas as
classes e chame o método.'''

class Animal:

    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return print("Som genérico")
    
class Cachorro(Animal):

    def __init__(self, nome):
       self.nome = nome

    def emitir_som(self):
        return print("Latido!")

dogTimido = Animal("Timido")
dog = Cachorro("Fred")

dogTimido.emitir_som()
dog.emitir_som()