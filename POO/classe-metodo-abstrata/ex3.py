'''Crie uma classe abstrata Arquivo com um método abrir. 
Implemente subclasses ArquivoTexto e ArquivoImagem que exibam mensagens diferentes ao abrir.'''

from abc import ABC, abstractmethod

class Arquivo(ABC):
    @abstractmethod
    def abrir(self):
        pass

class ArquivoTexto(Arquivo):
    def __init__(self, nome):
        self.nome = nome
    
    def abrir(self):
        return print(f"Abrindo arquivo {self.nome}")

class ArquivoImagem(Arquivo):
    def __init__(self, nome):
        self.nome = nome
    
    def abrir(self):
        return print(f"Abrindo arquivo {self.nome}")

arquivo1 = ArquivoTexto("documento.txt")
arquivo1.abrir()

arquivo2 = ArquivoImagem("foto.jpg")
arquivo2.abrir()

