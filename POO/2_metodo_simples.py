class Pessoa:
    def __init__(self, nome, idade): # Método construtor
        self.nome = nome # Atributo de instância
        self.idade = idade # Atributo de instância

    def apresentar(self): # Método de instância
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
    
pessoa = Pessoa("Kaymmi", 19)

print(pessoa.apresentar())