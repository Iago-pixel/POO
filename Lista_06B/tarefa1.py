import datetime as dt

class Cliente:
    def __init__(self, id, n, e, f):
        self.id = id
        self.nome = n
        self.email = e
        self.fone = f

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def fone(self):
        return self.__fone

    @id.setter
    def id(self, id):
        if id < 1:
            raise ValueError("O valor do id deve ser maior que 0!")
        self.__id = id

    @nome.setter
    def nome(self, n):
        if n == "":
            raise ValueError("O nome é obrigatório!")
        self.__nome = n

    @email.setter
    def email(self, e):
        if e == "":
            raise ValueError("O e-mail é obrigatório!")
        if not "@" in e:
            raise ValueError("Esse e-mail é inválido!")
        self.__email = e

    @fone.setter
    def fone(self, f):
        if f == "":
            raise ValueError("O telefone é obrigatório!")
        self.__fone = f

    def to_string(self):
        return f"id {self.id} - {self.nome} - {self.email} - tel. {self.fone}"

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "fone": self.fone
        }

    @classmethod
    def from_json(cls, dic):
        return cls(**dic)


class Venda:
    def __init__(self, id, id_cl):
        self.id = id
        self.data = dt.datetime.now()
        self.carrinho = True
        self.total = 0
        self.id_cliente = id_cl

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.__data

    @property
    def carrinho(self):
        return self.__carrinho

    @property
    def total(self):
        return self.__total

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id.setter
    def id(self, id):
        if id < 1:
            raise ValueError("O valor do id deve ser maior que 0!")
        self.__id = id

    @data.setter
    def data(self, d):
        self.__data = d

    @carrinho.setter
    def carrinho(self, c):
        self.__carrinho = c

    @total.setter
    def total(self, t):
        if t < 0:
            raise ValueError("O total deve ser positivo!")
        self.__total = t

    @id_cliente.setter
    def id_cliente(self, id_cl):
        if id_cl < 1:
            raise ValueError("O valor do id do cliente deve ser maior que 0!")
        self.__id_cliente = id_cl

    def to_string(self):
        id = self.id
        data = self.data.strftime("%d/%m/%Y")
        carrinho = "Está no carrinho" if self.carrinho else "Não está no carrinho"
        total = f"R$ {self.total:.2f}"
        id_cliente = self.id_cliente
        return f"id {id} - criado em {data} - {carrinho} - total: {total} - id do cliente {id_cliente}"

    def to_json(self):
        return {
            "id": self.id,
            "data": self.data,
            "carrinho": self.carrinho,
            "total": self.total,
            "id_cliente": self.id_cliente
        }

    @classmethod
    def from_json(cls, dic):
        venda = cls(dic["id"], dic["id_cliente"])
        venda.data = dic["data"]
        venda.carrinho = dic["carrinho"]
        venda.total = dic["total"]
        return venda


class Categoria:
    def __init__(self, id, d):
        self.id = id
        self.descricao = d

    @property
    def id(self):
        return self.__id

    @property
    def descricao(self):
        return self.__descricao

    @id.setter
    def id(self, id):
        if id < 1:
            raise ValueError("O valor do id deve ser maior que 0!")
        self.__id = id

    @descricao.setter
    def descricao(self, d):
        if d == "":
            raise ValueError("A descrição é obrigatória!")
        self.__descricao = d

    def to_string(self):
        return f"id {self.id} - {self.descricao}"

    def to_json(self):
        return {
            "id": self.id,
            "descricao": self.descricao
        }

    @classmethod
    def from_json(cls, dic):
        return cls(**dic)


class Produto:
    def __init__(self, id, d, p, e, id_cat):
        self.id = id
        self.descricao = d
        self.preco = p
        self.estoque = e
        self.id_categoria = id_cat

    @property
    def id(self):
        return self.__id

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @property
    def estoque(self):
        return self.__estoque

    @property
    def id_categoria(self):
        return self.__id_categoria

    @id.setter
    def id(self, id):
        if id < 1:
            raise ValueError("O valor do id deve ser maior que 0!")
        self.__id = id

    @descricao.setter
    def descricao(self, d):
        if d == "":
            raise ValueError("A descrição é obrigatória!")
        self.__descricao = d

    @preco.setter
    def preco(self, p):
        if p < 0:
            raise ValueError("O preço deve ser positivo!")
        self.__preco = p

    @estoque.setter
    def estoque(self, e):
        if e < 0:
            raise ValueError("O estoque deve ser positivo!")
        self.__estoque = e

    @id_categoria.setter
    def id_categoria(self, id_cat):
        if id_cat < 1:
            raise ValueError("O valor do id_categoria deve ser maior que 0!")
        self.__id_categoria = id_cat

    def to_string(self):
        return f"id {self.id} - {self.descricao} - R$ {self.preco:.2f} - N° no estoque: {self.estoque} - id da categoria {self.id_categoria}"

    def to_json(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "preco": self.preco,
            "estoque": self.estoque,
            "id_categoria": self.id_categoria
        }

    @classmethod
    def from_json(cls, dic):
        return cls(**dic)


class VendaItem:
    def __init__(self, id, q, p, id_ven, id_pr):
        self.id = id
        self.qtd = q
        self.preco = p
        self.id_venda = id_ven
        self.id_produto = id_pr

    @property
    def id(self):
        return self.__id

    @property
    def qtd(self):
        return self.__qtd

    @property
    def preco(self):
        return self.__preco

    @property
    def id_venda(self):
        return self.__id_venda

    @property
    def id_produto(self):
        return self.__id_produto

    @id.setter
    def id(self, id):
        if id < 1:
            raise ValueError("O valor do id deve ser maior que 0!")
        self.__id = id

    @qtd.setter
    def qtd(self, q):
        if q < 0:
            raise ValueError("A quantidade em estoque deve ser positiva!")
        self.__qtd = q

    @preco.setter
    def preco(self, p):
        if p < 0:
            raise ValueError("O preço deve ser positivo!")
        self.__preco = p

    @id_venda.setter
    def id_venda(self, id_ven):
        if id_ven < 1:
            raise ValueError("O valor do id da venda deve ser maior que 0!")
        self.__id_venda = id_ven

    @id_produto.setter
    def id_produto(self, id_pr):
        if id_pr < 1:
            raise ValueError("O valor do id do produto deve ser maior que 0!")
        self.__id_produto = id_pr

    def to_string(self):
        return f"id {self.id} - quantidade: {self.qtd} - R$ {self.preco:.2f} - id_venda {self.id_venda} - id_produto {self.id_produto}"

    def to_json(self):
        return {
            "id": self.id,
            "qtd": self.qtd,
            "preco": self.preco,
            "id_venda": self.id_venda,
            "id_produto": self.id_produto
        }

    @classmethod
    def from_json(cls, dic):
        return cls(**dic)