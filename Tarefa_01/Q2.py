class Pais:
    def __init__(self, n, p, a):
        self.set_nome(n)
        self.set_populacao(p)
        self.set_area(a)

    def set_nome(self, n):
        if n == "":
            raise ValueError("Nome é obrigatório!")
        self.__nome = n

    def set_populacao(self, p):
        if p < 0:
            raise ValueError("População não pode ser negativa!")
        self.__populacao = p

    def set_area(self, a):
        if a < 0:
            raise ValueError("Área não pode ser negativa!")
        self.__area = a

    def get_nome(self):
        return self.__nome

    def get_populacao(self):
        return self.__populacao

    def get_area(self):
        return self.__area

    def densidade(self):
        return self.__populacao / self.__area

    def __str__(self):
        return f"{self.__nome} possui {self.__populacao} habitantes e {self.__area} km²."


class PaisUI:
    @classmethod
    def main(cls):
        while True:
            opcao = cls.menu()
            if opcao == 1:
                cls.calculo()
            if opcao == 2:
                break

    @staticmethod
    def menu():
        print("1 - Calcular, 2 - Fim")
        return int(input())

    @staticmethod
    def calculo():
        n = input("Digite o nome do país: ")
        p = int(input("Digite o número de habitantes: "))
        a = float(input("Digite a área do país: "))
        pais = Pais(n, p, a)
        print(pais)
        print(f"Densidade: {pais.densidade()}")


PaisUI.main()
