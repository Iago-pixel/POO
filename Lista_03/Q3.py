class Conversor:
    def __init__(self, num):
        self.set_num(num)

    def set_num(self, num):
        if num < 0:
            raise ValueError("Inteiro deve ser positivo")
        self.__num = num

    def get_num(self):
        return self.__num

    def binario(self):
        b = ""
        for i in range(64, -1, -1):
            if 2**i <= self.__num:
                b += "1"
                self.__num -= 2**i
            elif b != "":
                b += "0"
        if b == "":
            b = "0"
        return b

    def __str__(self):
        return f"Base 10: {self.__num} | Base 2: {self.binario()}"

conversor = Conversor(423)
print(conversor)
