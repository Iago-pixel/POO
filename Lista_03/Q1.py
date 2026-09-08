class Retangulo:
    def __init__(self, b, h):
        self.set_base(b)
        self.set_altura(h)

    def set_base(self, b):
        if b > 0:
            self.__b = b

    def set_altura(self, h):
        if h > 0:
            self.__h = h

    def get_base(self):
        return self.__b

    def get_altura(self):
        return self.__h

    def calc_area(self):
        return self.__b * self.__h

    def calc_diagonal(self):
        return (self.__b ** 2 + self.__h ** 2) ** 0.5
    
    def __str__(self):
        return f"Seu retângulo tem base igual a {self.__b} e altura igual a{self.__h}."