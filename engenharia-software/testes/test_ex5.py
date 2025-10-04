'''Implemente uma função calcular_frete(peso, distancia) com a regra:

Até 10kg → R$ 5 por km.
Acima de 10kg → R$ 7 por km.
Crie testes de aceitação para validar os requisitos.'''

def calcular_frete(peso, distancia):
    if peso <= 10:
        return 5 * distancia
    else:
        return 7 * distancia
    
def test_calcular_frete_ate_10kg():
    assert calcular_frete(10, 2) == 10

def test_calcular_frete_acima_10kg():
    assert calcular_frete(11, 2) == 14  
    
def test_calcular_frete_zero_distancia():
    assert calcular_frete(5, 0) == 0