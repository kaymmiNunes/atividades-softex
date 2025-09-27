'''Crie as classes Universidade e Departamento.
A universidade é responsável por criar departamentos.
Cada departamento tem nome e quantidade de professores.
Crie uma universidade com 3 departamentos diferentes e liste-os.'''

class Departamento:

    def __init__(self, nome, professores):
        self.nome = nome
        self.professores = professores

class Universidade:

    def __init__(self):
        self.departamentos = []
        
    def criar_departamento(self, departamento: Departamento):
        self.departamentos.append(departamento)
    
    def listar_departamentos(self):
        for departamento in self.departamentos:
            print(f"Departamento: {departamento.nome} - Quantidade de professores: {departamento.professores}")

    
uepb = Universidade()

uepb.criar_departamento(Departamento("Computação", 30))
uepb.criar_departamento(Departamento("Matemática", 20))
uepb.criar_departamento(Departamento("Física", 15))

uepb.listar_departamentos()

