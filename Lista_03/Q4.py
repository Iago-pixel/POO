class EquacaoDoIIGrau:
    def __init__(self, a, b, c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    def set_a(self, a):
        self.__a = a

    def set_b(self, b):
        self.__b = b

    def set_c(self, c):
        self.__c = c

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def delta(self):
        return self.__b**2 - 4*self.__a*self.__c

    def tem_raizes_reais(self):
        return self.delta() >= 0

    def raiz_1(self):
        if self.tem_raizes_reais():
            return (-self.__b + self.delta()**0.5) / 2*self.__a
        else:
            return None

    def raiz_2(self):
        if self.delta() > 0:
            return (-self.__b - self.delta()**0.5) / 2*self.__a

    def __str__(self):
        equacao = f"{self.__a}x² "
        if self.__b < 0:
            equacao += f"- {self.__b*-1}x "
        else:
            equacao += f"+ {self.__b}x "
        if self.__c < 0:
            equacao += f"- {self.__c*-1}"
        else:
            equacao += f"+ {self.__c}"

print("x² - 5x + 6 = 0")
equacao = EquacaoDoIIGrau(1, -5, 6)
print(f"Delta =", equacao.delta())
print("Tem raiz?")
if equacao.tem_raizes_reais():
    print("Sim")
else:
    print("Não")
print("x1 =", equacao.raiz_1())
print("x2 =", equacao.raiz_2())
print("---------")

print("x² - 6x + 9 = 0")
equacao = EquacaoDoIIGrau(1, -6, 9)
print(f"Delta =", equacao.delta())
print("Tem raiz?")
if equacao.tem_raizes_reais():
    print("Sim")
else:
    print("Não")
print("x1 =", equacao.raiz_1())
print("x2 =", equacao.raiz_2())
print("---------")

print("x² + 2x + 5 = 0")
equacao = EquacaoDoIIGrau(1, 2, 5)
print(f"Delta =", equacao.delta())
print("Tem raiz?")
if equacao.tem_raizes_reais():
    print("Sim")
else:
    print("Não")
print("x1 =", equacao.raiz_1())
print("x2 =", equacao.raiz_2())
