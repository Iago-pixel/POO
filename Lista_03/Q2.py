class Frete:
    def __init__(self, distancia, peso):
        self.set_distancia(distancia)
        self.set_peso(peso)

    def set_distancia(self, distancia):
        if distancia < 0:
            raise ValueError("Distância deve ser positiva!")
        self.__distancia = distancia

    def set_peso(self, peso):
        if peso < 0:
            raise ValueError("Peso deve ser positivo!")
        self.__peso = peso

    def get_distancia(self):
        return self.__distancia

    def get_peso(self):
        return self.__peso

    def calc_frete(self):
        return (self.__peso * self.__distancia) / 100

    def __str__(self):
        return f"Distância: {self.__distancia}; Peso: {self.__peso}"

print("--TESTE--")
print("Criando obj com distancia 100km e peso 500kg")
frete = Frete(100, 500)
print(frete)
print(f"Frete: R$ {frete.calc_frete():.2f}")