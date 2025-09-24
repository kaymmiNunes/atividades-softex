'''Crie as classes Playlist e Musica.
Uma playlist pode ter várias músicas.
Cada música tem título e cantor.
Adicione músicas à playlist e exiba todas.'''

class Musica:

    def __init__(self, titulo, cantor):
        self.titulo = titulo
        self.cantor = cantor

class Playlist:

    def __init__(self, nome_playlist):
        self.nome_playlist = nome_playlist
        self.musicas = []
    
    def adicionar_musica(self, musica: Musica):
        self.musicas.append(musica)
    
    def mostrar_playlist(self): 
        print(f"Playlist: {self.nome_playlist}")
        for i, musica in enumerate(self.musicas):
            print(f"{i + 1}. {musica.titulo} - {musica.cantor}")

play1 = Playlist("Favoritas")

musica1 = Musica("Imagine", "John Lennon")
play1.adicionar_musica(musica1)

musica2 = Musica("Bohemian Rhapsody", "Queen")
play1.adicionar_musica(musica2)

musica3 = Musica("Billie Jean", "Michael Jackson")
play1.adicionar_musica(musica3)

play1.mostrar_playlist()