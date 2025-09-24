'''Crie as classes Empresa e Funcionario.
A empresa cria e gerencia seus funcionários.
Cada funcionário tem nome e cargo.
Crie uma empresa e adicione 3 funcionários.
Mostre o nome de cada funcionário.
'''

class Funcionario:
    
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

class Empresa:

    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)

    def mostrar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f'Nome: {funcionario.nome}, Cargo: {funcionario.cargo}')

# Exemplo de uso

empresa = Empresa()

empresa.adicionar_funcionario(Funcionario('André', 'Desenvolvedor'))
empresa.adicionar_funcionario(Funcionario("Bob", "Designer"))
empresa.adicionar_funcionario(Funcionario("Charlie", "Gerente de Projetos"))

empresa.mostrar_funcionarios()