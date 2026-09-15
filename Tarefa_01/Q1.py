class Viagem:
    def __init__(self, destino, distancia, litros):
        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_litros(litros)

    def set_destino(self, destino):
        self.__destino = destino

    def set_distancia(self, distancia):
        if distancia < 0:
            raise ValueError("Distância deve ser um valor positivo!")
        self.__distancia = distancia

    def set_litros(self, litros):
        if litros < 0:
            raise ValueError("Litros deve ser um valor positivo!")
        self.__litros = litros

    def get_destino(self):
        return self.__destino

    def get_distancia(self):
        return self.__distancia

    def get_litros(self):
        return self.__litros

    def consumo(self):
        return self.__distancia / self.__litros

    def __str__(self):
        return f"Para ir para {self.__destino} você correu {self.__distancia} km e gastou {self.__litros} litros."


class ViagemUI:
    @classmethod
    def main(cls):
        while True:
            if cls.menu() == 2:
                break
            cls.calculo()

    @staticmethod
    def menu():
        print("1 - Calcular, 2 - Fim")
        return int(input())

    @staticmethod
    def calculo():
        destino = input("Digite o destino: ")
        distancia = float(input("Digite a distância em km: "))
        litros = float(input("Digite o gasto de gasolina em litros: "))
        viagem = Viagem(destino, distancia, litros)
        print(viagem)
        print(viagem.consumo())

ViagemUI.main()
