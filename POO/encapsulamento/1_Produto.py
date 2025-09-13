class Produto:
    def __init__(self, nome, preco): # Método construtor
        self.nome = nome
        self.__preco = preco

# Getter
    def get_preco(self): # Método de instância
        if self.__preco < 0:
            return "O preço não pode ser negativo."
        else:
            return self.__preco

# Setter
    def set_preco(self, preco): # Método de instância
        if preco < 0:
            return "O preço não pode ser negativo."
        else:
            self.__preco = preco
            return self.__preco

produto = Produto("Caneta", 2.5)

print(produto.get_preco())
print(produto.set_preco(10))
print(produto.get_preco())
print(produto.set_preco(-5))