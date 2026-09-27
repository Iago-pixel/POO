class Cliente:
    def __init__(self, nome, cpf, limite):
        self.nome = nome
        self.cpf = cpf
        self.limite = limite
        self.__socio = None

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def limite(self):
        if self.__socio == None:
            return self.__limite
        return self.__limite + self.__socio.__limite

    @property
    def socio(self):
        return self.__socio

    @nome.setter
    def nome(self, nome):
        if nome == "":
            raise ValueError("Nome é obrigatório!")
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        if cpf == "":
            raise ValueError("Nome é obrigatório!")
        self.__cpf = cpf

    @limite.setter
    def limite(self, limite):
        if limite < 0:
            raise ValueError("Limite deve ser positivo!")
        self.__limite = limite

    @socio.setter
    def socio(self, c):
        if self.__socio != None:
            self.__socio.__socio = None
        if c.__socio != None:
            c.__socio.__socio = None
        self.__socio = c
        c.__socio = self

    def __str__(self):
        return f"Nome: {self.__nome}; CPF: {self.__cpf}; Limite: {self.__limite:.2f}."


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.__clientes = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if nome == "":
            raise ValueError("Nome é obrigatório!")
        self.__nome = nome

    def inserir(self, c):
        self.__clientes.append(c)

    def listar(self):
        return self.__clientes

    def __str__(self):
        return self.__nome


class UI:
    empresas = []

    @classmethod
    def main(cls):
        while True:
            print("MENU PRINCIPAL")
            opcao_menu_principal = cls.menu_principal()
            if opcao_menu_principal == 0:
                break
            if opcao_menu_principal == 1:
                print("INSERIR EMPRESA")
                cls.inserir_empresa()
            if opcao_menu_principal == 2:
                while True:
                    print("MENU DE EMPRESAS")
                    opcao_menu_empresas = cls.menu_empresas()
                    if opcao_menu_empresas == 0:
                        break
                    elif opcao_menu_empresas <= len(cls.empresas):
                        empresa = cls.empresas[opcao_menu_empresas - 1]
                        while True:
                            print(f"MENU DA EMPRESA ({empresa.nome})")
                            opcao_menu_empresa = cls.menu_empresa()
                            if opcao_menu_empresa == 0:
                                break
                            if opcao_menu_empresa == 1:
                                print("INSERIR CLIENTE")
                                cls.inserir_cliente(empresa)
                            if opcao_menu_empresa == 2:
                                while True:
                                    print(f"MENU DE CLIENTES ({empresa.nome})")
                                    opcao_menu_clientes = cls.menu_clientes(empresa)
                                    if opcao_menu_clientes == 0:
                                        break
                                    elif opcao_menu_clientes <= len(empresa.listar()):
                                        cliente = empresa.listar()[opcao_menu_clientes - 1]
                                        while True:
                                            print(f"MENU DO CLIENTE")
                                            opcao_menu_cliente = cls.menu_cliente(cliente)
                                            if opcao_menu_cliente == 0:
                                                break
                                            if opcao_menu_cliente == 1:
                                                while True:
                                                    print(f"MENU DE SOCIEDADE ({cliente.nome})")
                                                    opcao_menu_sociedade = cls.menu_sociedade(empresa, cliente)
                                                    if opcao_menu_sociedade == 0:
                                                        break
                                                    elif opcao_menu_sociedade <= len(empresa.listar()):
                                                        socio = empresa.listar()[opcao_menu_sociedade - 1]
                                                        cliente.socio = socio
                                                        print(f"Cliente {socio.nome} agora é socio de {cliente.nome}!")
                                                        break

    @staticmethod
    def menu_principal():
        print("1 - Inserir empresa, 2 - Listar empresas, 0 - Sair")
        return int(input())

    @classmethod
    def inserir_empresa(cls):
        nome = input("Digite o nome da empresa: ")
        empresa = Empresa(nome)
        cls.empresas.append(empresa)
        print(f"Empresa {nome} inserida!")

    @classmethod
    def menu_empresas(cls):
        for indece, empresa in enumerate(cls.empresas):
            print(f"{indece + 1} - {empresa}")
        print("0 - Voltar ao menu principal")
        return int(input())

    @staticmethod
    def inserir_cliente(empresa):
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF: ")
        limite = int(input("Digite o limite: "))
        cliente = Cliente(nome, cpf, limite)
        empresa.inserir(cliente)
        print(f"Cliente {nome} inserido na empresa {empresa.nome}!")

    @staticmethod
    def menu_empresa():
        print("1 - Adicionar cliente")
        print("2 - listar cliente")
        print("0 - Voltar ao menu de empresas")
        return int(input())

    @staticmethod
    def menu_clientes(empresa):
        for indice, cliente in enumerate(empresa.listar()):
            print(f"{indice + 1} - {cliente.nome}")
        print("0 - Voltar ao menu de empresas")
        return int(input())

    @staticmethod
    def menu_cliente(cliente):
        print(f"Nome: {cliente.nome}")
        print(f"CPF: {cliente.cpf}")
        print(f"Limite: {cliente.limite}")
        if cliente.socio:
            print(f"Socio: {cliente.socio.nome}")
        else:
            print("Socio: N/A")
        print("1 - Adicionar/Alterar socio, 0 - Voltar ao menu de clientes")
        return int(input())

    @staticmethod
    def menu_sociedade(empresa, cliente_atual):
        for indice, cliente in enumerate(empresa.listar()):
            if cliente_atual.cpf != cliente.cpf:
                print(f"{indice + 1} - {cliente.nome}")
        print("0 - Voltar ao menu do cliente")
        return int(input())

UI.main()
