class Carro:
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.__velocidade = velocidade

    def acelerar(self, incremento):
        self.__velocidade += incremento
        return self.__velocidade 

    def frear(self, decremento):
        self.__velocidade -= decremento
        return self.__velocidade
    

carro1 = Carro("Civic", 0)

print(carro1.acelerar(10))
print(carro1.acelerar(10))
print(carro1.acelerar(10))
print(carro1.acelerar(10))
print(carro1.acelerar(10))
print(carro1.frear(10))
print(carro1.frear(10))
print(carro1.frear(10))
print(carro1.frear(10))
print(carro1.frear(10))

