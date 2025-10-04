'''Implemente uma função de autenticação que rejeita senhas menores que 8 caracteres.

Escreva testes cobrindo cenários de sucesso e falha.'''

def senha(senha):
    if len(senha) >= 8:
        return True
    else:
        return False
    
def test_senha_menor():
    assert senha("1234567") == False
    
def test_senha_ok():
    assert senha("12345678") == True
    