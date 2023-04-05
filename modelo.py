class Programas:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return "Nome: {} - Ano: {} - Likes: {}".format(self.nome, self.ano, self.likes)

class Filme(Programas):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return "Nome: {} - Duração: {} min - Ano: {} - Likes: {}".format(self.nome, self.duracao, self.ano, self.likes)

class Serie(Programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return "Nome: {} - Temporadas: {} - Ano: {} - Likes: {}".format(self.nome, self.temporadas, self.ano, self.likes)

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
creed = Filme("Creed III", 2023, 160)
vikings = Serie("vikings", 2013, 8)
demolidor = Serie("Demolidor", 2015, 3)

vingadores.dar_likes()
vingadores.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
creed.dar_likes()
creed.dar_likes()
creed.dar_likes()
creed.dar_likes()
vikings.dar_likes()


filmes_e_series = [vingadores, vikings, demolidor, creed]
playlist_fds = Playlist("Maratona final de semana: ", filmes_e_series)

print("A playlist possui {} programas.".format(len(playlist_fds)))
print("----------------------------------------------------------------------------")
for programas in playlist_fds:
    print(programas)










