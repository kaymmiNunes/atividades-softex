'''Crie as classes Livro e Pagina.
Cada livro cria várias páginas internamente.
Cada página tem um número e um pequeno texto.
Mostre o conteúdo do livro listando todas as páginas.
'''

class Livro:

    def __init__(self):
        self.paginas = []
    
    def adicionar_pagina(self, numero, texto):
        pagina = Pagina(numero, texto)
        self.paginas.append(pagina)

    def mostrar_conteudo(self):
        for pagina in self.paginas:
            print(f'Página {pagina.numero}: {pagina.texto}')

class Pagina:

    def __init__(self, numero, texto):
        self.numero = numero
        self.texto = texto

# Exemplo de uso
livro = Livro()
livro.adicionar_pagina(1, "Era uma vez...")
livro.adicionar_pagina(2, "Em um reino distante...")
livro.adicionar_pagina(3, "E viveram felizes para sempre.")

livro.mostrar_conteudo()
