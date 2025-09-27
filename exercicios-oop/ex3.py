'''Exercício 3: Herança com Construtores
Crie uma classe base Funcionario com um construtor que inicializa nome e salario. Crie
uma classe filha Gerente que herda de Funcionario. O construtor de Gerente deve aceitar
um atributo adicional departamento e usar super().__init__ para passar nome e salario para
a classe base.'''

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):

    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento
    
gerente = Gerente("Alice", 8000, "Vendas")

print(f'Nome: {gerente.nome}, Salário: {gerente.salario}, Departamento: {gerente.departamento}')

    