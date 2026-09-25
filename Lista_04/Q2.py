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
        self.__socio = c
        c.__socio = self
    
    def __str__(self):
        return f"Nome: {self.__nome}; CPF: {self.__cpf}; Limite: {self.__limite:.2f}."
