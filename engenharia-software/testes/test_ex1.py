'''Crie uma função eh_par(numero) que retorna True se o número for par.
Escreva 3 testes unitários cobrindo casos positivos e negativos.'''

def eh_par(numero):
    return numero % 2 == 0

def test_eh_par_com_par():
    assert eh_par(2) == True 

def test_eh_par_com_negativo():
    assert eh_par(-2) == True 

def test_eh_par_com_impar():
    assert eh_par(3) == True 

def test_eh_par_com_zero():
    assert eh_par(0) == True

