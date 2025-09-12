class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
    
pessoa = Pessoa("Kaymmi", 19)
print(pessoa.apresentar())