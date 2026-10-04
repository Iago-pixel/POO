import datetime as dt
import enum


class Estagio:
    def __init__(self, i, est, emp):
        self.id = i
        self.estagiario = est
        self.empresa = emp
        self.__situacao = SituacaoEstagio.CADASTRADO

    @property
    def id(self):
        return self.__id

    @property
    def estagiario(self):
        return self.__estagiario

    @property
    def empresa(self):
        return self.__empresa

    @id.setter
    def id(self, i):
        if i <= 0:
            raise ValueError("Id deve ser maior que 0!")
        self.__id = i

    @estagiario.setter
    def estagiario(self, est):
        if est == "":
            raise ValueError("Nome do estagiário é obrigatório!")
        self.__estagiario = est

    @empresa.setter
    def empresa(self, emp):
        if emp == "":
            raise ValueError("Nome da empresa é obrigatório!")
        self.__empresa = emp

    def iniciar(self, data):
        if data <= dt.datetime.now():
            self.__data_inicio = data
            self.__situacao = SituacaoEstagio.INICIADO
            return True
        return False

    def cancelar(self, data):
        if data <= dt.datetime.now():
            self.__data_cancelamento = data
            self.__situacao = SituacaoEstagio.CANCELADO
            return True
        return False

    def finalizar(self, data):
        if data <= dt.datetime.now():
            self.__data_fim = data
            self.__situacao = SituacaoEstagio.FINALIZADO
            return True
        return False

    @property
    def data_inicio(self):
        return self.__data_inicio

    @property
    def data_cancelamento(self):
        return self.__data_cancelamento

    @property
    def data_fim(self):
        return self.__data_fim

    def tempo_estagio(self):
        if self.situacao.name == "CADASTRADO":
            raise ValueError("Estágio não foi iniciado!")
        if self.situacao.name == "INICIADO":
            return dt.datetime.now() - self.data_inicio
        if self.situacao.name == "CANCELADO":
            return self.data_cancelamento - self.data_inicio
        if self.situacao.name == "FINALIZADO":
            return self.data_fim - self.data_inicio

    @property
    def situacao(self):
        return self.__situacao

    def __str__(self):
        txt = f"{self.id} - {self.estagiario} da empresa {self.empresa}"
        if self.situacao.name == "CADASTRADO":
            txt += " está cadastrado."
        else:
            txt += f" iniciou o estágio dia {self.data_inicio.strftime('%d/%m/%Y')}"
        if self.situacao.name == "INICIADO":
            txt += "."
        if self.situacao.name == "CANCELADO":
            txt += f" e teve o vínculo cancelado dia {self.data_cancelamento.strftime('%d/%m/%Y')}."
        if self.situacao.name == "FINALIZADO":
            txt += f" e teve o vículo finalizado dia {self.data_fim.strftime('%d/%m/%Y')}."
        return txt


class SituacaoEstagio(enum.Enum):
    CADASTRADO = 1
    INICIADO = 2
    CANCELADO = 3
    FINALIZADO = 4


class UI:
    estagios = []
    id_atual = 0

    @classmethod
    def main(cls):
        while True:
            opcao_selecionada = cls.menu()
            if opcao_selecionada == 1:
                cls.inserir()
            if opcao_selecionada == 2:
                cls.iniciar()
            if opcao_selecionada == 3:
                cls.cancelar()
            if opcao_selecionada == 4:
                cls.finalizar()
            if opcao_selecionada == 5:
                cls.listar_por_empresa()
            if opcao_selecionada == 6:
                cls.listar_por_estagiario()
            if opcao_selecionada == 7:
                cls.listar_por_situacao()
            if opcao_selecionada == 8:
                break
            input("Aperte enter para voltar ao menu.")

    @staticmethod
    def menu():
        print("MENU PRINCIPAL")
        print("1 - Inserir um estágio;")
        print("2 - Iniciar um estágio;")
        print("3 - Cancelar um estágio;")
        print("4 - Finalizar um estágio;")
        print("5 - Listar todos os estágios ordenados por empresa;")
        print("6 - Listar todos os estágios ordenados por estagiário;")
        print("7 - Listar os estágios por situação;")
        print("8 - Sair;")
        return int(input())

    @staticmethod
    def menu_situacao():
        print("1 - Cadastrados;")
        print("2 - Iniciados;")
        print("3 - Cancelados;")
        print("4 - Finalizado;")
        return int(input())

    @classmethod
    def inserir(cls):
        print("INSERIR ESTÁGIO")

        cls.id_atual += 1
        i = cls.id_atual
        est = input("Digite o nome do estagiário: ")
        emp = input("Digite o nome da empresa: ")

        estagio = Estagio(i, est, emp)
        cls.estagios.append(estagio)

        print("Estágio inserido!")

    @classmethod
    def iniciar(cls):
        print("INICIAR UM ESTÁGIO")

        i = int(input("Digite o id do estágio: "))
        estagios_com_id = [estagio for estagio in cls.estagios if estagio.id == i]

        if len(estagios_com_id) == 0:
            print("Estágio não encontrado!")
            return

        data = input("Digite a data de inicio (dd/mm/aaa): ")
        dia, mes, ano = map(int, data.split("/"))
        data_dt = dt.datetime(ano, mes, dia)

        estagio = estagios_com_id[0]
        if estagio.iniciar(data_dt):
            print("Estágio iniciado!")
        else:
            print("Data inválida, digite a data atual ou uma data que já passou!")

    @classmethod
    def cancelar(cls):
        print("CANCELAR UM ESTÁGIO")

        i = int(input("Digite o id do estágio: "))
        estagios_com_id = [estagio for estagio in cls.estagios if estagio.id == i]

        if len(estagios_com_id) == 0:
            print("Estágio não encontrado!")
            return

        data = input("Digite a data de cancelamento (dd/mm/aaa): ")
        dia, mes, ano = map(int, data.split("/"))
        data_dt = dt.datetime(ano, mes, dia)

        estagio = estagios_com_id[0]
        if estagio.cancelar(data_dt):
            print("Estágio cancelado!")
        else:
            print("Data inválida, digite a data atual ou uma data que já passou!")

    @classmethod
    def finalizar(cls):
        print("FINALIZAR UM ESTÁGIO")

        i = int(input("Digite o id do estágio: "))
        estagios_com_id = [estagio for estagio in cls.estagios if estagio.id == i]

        if len(estagios_com_id) == 0:
            print("Estágio não encontrado!")
            return

        data = input("Digite a data de finalização (dd/mm/aaa): ")
        dia, mes, ano = map(int, data.split("/"))
        data_dt = dt.datetime(ano, mes, dia)

        estagio = estagios_com_id[0]
        if estagio.finalizar(data_dt):
            print("Estágio finalizado!")
        else:
            print("Data inválida, digite a data atual ou uma data que já passou!")

    @classmethod
    def listar_por_empresa(cls):
        if len(cls.estagios) == 0:
            print("Não há empresas!")
            return

        print("LISTA POR EMPRESA")

        estagios_por_empresa = sorted(cls.estagios, key=lambda e: e.empresa)
        for estagio in estagios_por_empresa:
            print(estagio)

    @classmethod
    def listar_por_estagiario(cls):
        if len(cls.estagios) == 0:
            print("Não há estagios!")
            return

        print("LISTA POR ESTAGIÁRIO")

        estagios_por_estagiario = sorted(cls.estagios, key=lambda e: e.estagiario)
        for estagio in estagios_por_estagiario:
            print(estagio)

    @classmethod
    def listar_por_situacao(cls):
        if len(cls.estagios) == 0:
            print("Não há estágios!")
            return

        print("LISTA POR SITUAÇÃO")

        opcao_selecionada = cls.menu_situacao()
        estagios_por_situacao = [estagio for estagio in cls.estagios if estagio.situacao.value == opcao_selecionada]

        if len(estagios_por_situacao) == 0:
            print("Nenhum estágio encontrado!")
            return

        for estagio in estagios_por_situacao:
            print(estagio)


UI.main()