'''Crie as classes Playlist e Musica.
A playlist cria músicas internamente.
Cada música tem título e duração.
Mostre todas as músicas de uma playlist.'''

class Musica:

    def __init__(self, titulo, timer):
        self.titulo = titulo
        self.timer = timer

class Playlist:
    
    def __init__(self):
        self.musicas = []

    def adicionar_musica(self, musica: Musica):
        self.musicas.append(musica)

    def mostrar_musicas(self):
        for i, musica in enumerate(self.musicas):
            print(f'Musica {i+1}: {musica.titulo} - Tempo: {musica.timer}')

melhores = Playlist()

melhores.adicionar_musica(Musica("Sozinho", "3:11"))
melhores.adicionar_musica(Musica("Tiro ao Álvaro", "2:44"))
melhores.adicionar_musica(Musica("Depois", "2:54"))

melhores.mostrar_musicas()


        

        