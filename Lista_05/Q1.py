import datetime as dt


class Paciente:
    def __init__(self, n, c, t, nasc):
        self.nome = n
        self.cpf = c
        self.telefone = t
        self.nascimento = nasc

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone

    @property
    def nascimento(self):
        return self.__nascimento

    @nome.setter
    def nome(self, n):
        if n == "":
            raise ValueError("Nome é obrigatório!")
        self.__nome = n

    @cpf.setter
    def cpf(self, c):
        if c == "":
            raise ValueError("CPF é obrigatório!")
        self.__cpf = c

    @telefone.setter
    def telefone(self, t):
        if t == "":
            raise ValueError("Telefone obrigatório!")
        self.__telefone = t

    @nascimento.setter
    def nascimento(self, nasc):
        self.__nascimento = nasc

    def idade(self):
        tempo_de_vida = dt.datetime.now() - self.nascimento
        dias_de_vida = tempo_de_vida.days
        anos_de_vida = dias_de_vida // 365
        dias_restantes = dias_de_vida % 365
        meses_restantes = dias_restantes // 30
        return f"{anos_de_vida} ano(s) e {meses_restantes} mese(s)."

    def __str__(self):
        return f"Paciente {self.nome}; cpf {self.cpf}; telefone {self.telefone}; nascimento {self.nascimento.strftime('%d/%m/%Y')}"


class UI:
    pacientes = []

    @classmethod
    def main(cls):
        while True:
            opcao_selecionada = cls.menu()
            if opcao_selecionada == 1:
                cls.inserir()
            if opcao_selecionada == 2:
                cls.listar_por_ordem_alfabetica()
            if opcao_selecionada == 3:
                cls.listar_por_ordem_de_idade()
            if opcao_selecionada == 4:
                break
            input("Aperte enter para voltar ao menu.")

    @staticmethod
    def menu():
        print("MENU PRINCIPAL")
        print("1 - Inserir um paciente;")
        print("2 - Listar pacientes por ordem alfabética;")
        print("3 - Listar pacientes por ordem de idade;")
        print("4 - Sair;")
        return int(input())

    @classmethod
    def inserir(cls):
        print("INSERIR PACIENTE")

        n = input("Digite o nome do paciente: ")
        c = input("Digite o CPF do paciente: ")
        t = input("Digite o telefone do paciente: ")

        nasc = input("Digite a data de nascimento do paciente (dd/mm/aaaa): ")
        dia, mes, ano = map(int, nasc.split("/"))
        nasc_dt = dt.datetime(ano, mes, dia)

        paciente = Paciente(n, c, t, nasc_dt)
        cls.pacientes.append(paciente)

        print("Paciente inserido!")

    @classmethod
    def listar_por_ordem_alfabetica(cls):
        print("LISTA DE PACIENTES POR ORDEM ALFABÉTICA")
        pacientes_por_ordem_alfabetica = sorted(cls.pacientes, key=lambda p: p.nome)
        for paciente in pacientes_por_ordem_alfabetica:
            print(paciente)

    @classmethod
    def listar_por_ordem_de_idade(cls):
        print("LISTA DE PACIENTES POR ORDEM DE IDADE")
        pacientes_por_ordem_de_idade = sorted(cls.pacientes, key=lambda p: p.idade())
        for paciente in pacientes_por_ordem_de_idade:
            print(paciente)


UI.main()