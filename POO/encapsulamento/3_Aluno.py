class Aluno:

    def __init__(self, nome, nota):
        self.nome = nome # Atributo público
        self.__nota = nota # Atributo privado

    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self.__nota = nova_nota
        else:
            print("Nota inválida. Deve ser entre 0 e 10.")

aluno1 = Aluno("Kaymmi", 7)

print("Nota inicial: ", aluno1.nota)
aluno1.nota = 9
print("Nota atual: ", aluno1.nota)
aluno1.nota = 11
print("Nota atual: ", aluno1.nota)


