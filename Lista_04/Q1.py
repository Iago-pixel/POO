class Musica:
    def __init__(self, titulo, artista, album):
        self.titulo = titulo
        self.artista = artista
        self.album = album

    @property
    def titulo(self):
        return self.__titulo

    @property
    def artista(self):
        return self.__artista

    @property
    def album(self):
        return self.__album

    @titulo.setter
    def titulo(self, titulo):
        if titulo == "":
            raise ValueError("Título é obrigatório!")
        self.__titulo = titulo

    @artista.setter
    def artista(self, artista):
        if artista == "":
            raise ValueError("Artista é obrigatório!")
        self.__artista = artista

    @album.setter
    def album(self, album):
        if album == "":
            raise ValueError("Album é obrigatório!")
        self.__album = album

    def __str__(self):
        return f"{self.__titulo} do artista {self.__artista} pertence ao album {self.__album}."


class PlayList:
    def __init__(self, nome, desc):
        self.nome = nome
        self.descricao = desc
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @nome.setter
    def nome(self, nome):
        if nome == "":
            raise ValueError("Nome da playlist é obrigatória!")
        self.__nome = nome

    @descricao.setter
    def descricao(self, desc):
        self.__descricao = desc

    def inserir(self, m):
        self.__musicas.append(m)

    def listar(self):
        return self.__musicas

    def __str__(self):
        return f"{self.__nome} possui {len(self.__musicas)} músicas."


class UI:
    playlists = [
        PlayList("Rock", "Batidas frenéticas de rock!!!"),
        PlayList("Clássica", "Música classica e erudita"),
        PlayList("MPB", "Músicas Populares Brasileiras"),
        PlayList("Outros", "")
    ]

    @classmethod
    def main(cls):
        while True:
            opcao_playlist = cls.menu_playlist()
            if opcao_playlist in [1, 2, 3, 4]:
                while True:
                    opcao_acao = cls.menu_acao()
                    if opcao_acao == 1:
                        cls.inserir_musica(cls.playlists[opcao_playlist - 1])
                    elif opcao_acao == 2:
                        cls.lista_musica(cls.playlists[opcao_playlist - 1])
                    elif opcao_acao == 3:
                        break
            elif opcao_playlist == 5:
                break

    @staticmethod
    def menu_playlist():
        print("1 - Rock, 2 - Clássica, 3 - MPB, 4 - Outros, 5 - Fim")
        return int(input())

    @staticmethod
    def menu_acao():
        print("1 - Inserir música, 2 - Listar músicas, 3 - Fim")
        return int(input())

    @staticmethod
    def inserir_musica(playlist):
        titulo = input("Digite o título da música: ")
        artista = input("Digite o nome do artista: ")
        album = input("Digite o nome do álbum: ")
        m = Musica(titulo, artista, album)
        playlist.inserir(m)
        print(f"Música inserida!")

    @staticmethod
    def lista_musica(playlist):
        for m in playlist.listar():
            print(m)


UI.main()
