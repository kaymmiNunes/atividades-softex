class Carro: 

    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
    
    def obter_marca(self):
        return self.marca
    
    def obter_ano(self):
        return self.ano
    
meu_carro = Carro("Honda", 2018)

print(meu_carro.obter_marca())
print(meu_carro.obter_ano())