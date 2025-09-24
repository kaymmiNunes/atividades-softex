'''Crie duas classes: Autor e Livro.
O autor tem nome e nacionalidade.
O livro tem título e um objeto autor.
Crie 2 autores e 3 livros.
Mostre no terminal o nome do livro e o nome do autor.'''

class Autor:

    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

class Livro:

    def __init__(self, titulo, autor: Autor):
        self.titulo = titulo
        self.autor = autor 
    
    def mostrar_livros(self):
        print(f"Livro: {self.titulo} - Autor: {self.autor.nome}")

autor1 = Livro("Dom Casmurro", Autor("Machado de Assis", "Brasil"))
autor2 = Livro("Hamlet", Autor("William Shakespeare", "Reino Unido"))
autor3 = Livro("Assassinato no Expresso do Oriente", Autor("Agatha Christie", "Reino Unido"))

autor1.mostrar_livros()
autor2.mostrar_livros()
autor3.mostrar_livros()