class Carro: 

    def __init__(self, marca, ano): # Método construtor
        self.marca = marca # Atributo de instância
        self.ano = ano # Atributo de instância

    def obter_marca(self): # Método de instância
        return self.marca

    def obter_ano(self): # Método de instância
        return self.ano
    
meu_carro = Carro("Honda", 2018) 


print(meu_carro.obter_marca())
print(meu_carro.obter_ano())