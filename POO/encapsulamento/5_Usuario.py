class Usuario:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    @property  
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
        else:
            print("O mínimo de caracteres é 6. Tente novamente.")
        
    def verificar_senha(self, senha_teste):
        if senha_teste == self.__senha:
            return True
        else:
            return False
          
Usuario1 = Usuario("kaymminunes@gmail.com", "123456" )

Usuario1.senha = "Teste"

print(Usuario1.verificar_senha("Senha?"))

print(Usuario1.verificar_senha("123456"))




