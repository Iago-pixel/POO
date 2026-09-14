class Data:
    def __init__(self, dia, mes, ano):
        self.set_data(f"{dia}/{mes}/{ano}")

    def set_data(self, data):
        dia, mes, ano = map(int, data.split("/"))
        self.__ano = ano

        if mes > 0 and mes <= 12:
            self.__mes = mes
        else:
            raise ValueError("Mês inválido!")

        if dia > 0 and dia < 29:
            self.__dia = dia
        elif mes == 2 and dia == 29 and ano % 4 == 0:
            if ano % 100 == 0 and ano % 400 != 0:
                raise ValueError("Dia inválido!")
            self.__dia = dia
        elif dia > 0 and dia < 31 and mes in [4, 6, 9, 11]:
            self.__dia = dia
        elif dia > 0 and dia <= 31:
            self.__dia = dia
        else:
            raise ValueError("Dia inválido!")

    def __str__(self):
        if self.__ano > 0:
            return f"{self.__dia:02d}/{self.__mes:02d}/{self.__ano}"
        return f"{self.__dia:02d}/{self.__mes:02d}/{self.__ano*-1} a.C."

print("14/09/2026")
data = Data(14,9,2026)
print(data)
print("---------")

print("29/02/2028")
data = Data(29,2,2028)
print(data)
print("---------")

print("29/03/1900 a.C.")
data = Data(29,3,-1900)
print(data)
print("---------")
