class Aluno:

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def ver_nome(self):
        return self.nome

    def ver_nota(self):
        return self.nota
    
    def verificar_aprovacao(self):
        if self.nota >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

aluno1 = Aluno("Kaymmi", 10)

print(aluno1.verificar_aprovacao())
