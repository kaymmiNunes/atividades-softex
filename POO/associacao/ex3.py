'''Crie as classes Time e Jogador.
Um time pode ter vários jogadores.
Crie 2 times com 3 jogadores cada.
Mostre a lista de jogadores de cada time.'''

class Jogador:

    def __init__(self, nome):
        self.nome = nome

class Time:

    def __init__(self, nome_time):
        self.nome_time = nome_time
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
    
    def mostrar_jogadores(self):
        print(f"\nTime: {self.nome_time}")
        for i, jogador in enumerate(self.jogadores):
            print(f"Jogador {i+1}: {jogador.nome}")

time1 = Time("Flamengo")
time2 = Time("Vasco")

jogador1 = Jogador("Neymar")
jogador2 = Jogador("C. Ronaldo")
jogador3 = Jogador("Raphinha")
jogador4 = Jogador("Messi")
jogador5 = Jogador("K. Mbappé")
jogador6 = Jogador("L. Messi")

time1.adicionar_jogador(jogador1)
time1.adicionar_jogador(jogador2)
time1.adicionar_jogador(jogador3)
time2.adicionar_jogador(jogador4)
time2.adicionar_jogador(jogador5)
time2.adicionar_jogador(jogador6)

time1.mostrar_jogadores()
time2.mostrar_jogadores()