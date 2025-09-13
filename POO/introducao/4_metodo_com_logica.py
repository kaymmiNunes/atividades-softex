class Aluno:

    def __init__(self, nome, nota): # Método construtor
        self.nome = nome # Atributo de instância
        self.nota = nota # Atributo de instância

    def ver_nome(self): # Método de instância
        return self.nome

    def ver_nota(self): # Método de instância
        return self.nota
    
    def verificar_aprovacao(self): # Método de instância
        if self.nota >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

aluno1 = Aluno("Kaymmi", 10)

print(aluno1.verificar_aprovacao())
