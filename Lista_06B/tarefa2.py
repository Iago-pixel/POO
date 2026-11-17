import json
from tarefa1 import Cliente, Venda, Categoria, Produto, VendaItem


class ClienteDAO:
    arquivo = "cliente.json"
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.objetos.append(obj)

    @classmethod
    def listar(cls):
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        raise IndexError("Cliente não encontrado!")

    @classmethod
    def atualizar(cls, novo_cliente):
        for i, cliente_atual in enumerate(cls.objetos):
            if novo_cliente.id == cliente_atual.id:
                cls.objetos[i] = novo_cliente
                return
        raise IndexError("Cliente não encontrado!")

    @classmethod
    def excluir(cls, id):
        for i, cliente_atual in enumerate(cls.objetos):
            if cliente_atual.id == id:
                cls.objetos.pop(i)
                return
        raise IndexError("Cliente não encontrado!")

    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open(cls.arquivo, mode="r") as arquivo:
            clientes_json = json.load(arquivo)
            for obj in clientes_json:
                c = Cliente.from_json(obj)
                cls.objetos.append(c)

    @classmethod
    def salvar(cls):
        clientes_json = [obj.to_json() for obj in cls.objetos]
        with open(cls.arquivo, mode="w") as arquivo:
            json.dump(clientes_json, arquivo)


class VendaDAO:
    arquivo = "venda.json"
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.objetos.append(obj)

    @classmethod
    def listar(cls):
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        raise IndexError("Venda não encontrado!")

    @classmethod
    def atualizar(cls, nova_venda):
        for i, venda_atual in enumerate(cls.objetos):
            if nova_venda.id == venda_atual.id:
                cls.objetos[i] = nova_venda
                return
        raise IndexError("Venda não encontrado!")

    @classmethod
    def excluir(cls, id):
        for i, venda_atual in enumerate(cls.objetos):
            if venda_atual.id == id:
                cls.objetos.pop(i)
                return
        raise IndexError("Venda não encontrado!")

    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open(cls.arquivo, mode="r") as arquivo:
            vendas_json = json.load(arquivo)
            for obj in vendas_json:
                v = Venda.from_json(obj)
                cls.objetos.append(v)

    @classmethod
    def salvar(cls):
        vendas_json = [obj.to_json() for obj in cls.objetos]
        with open(cls.arquivo, mode="w") as arquivo:
            json.dump(vendas_json, arquivo)


class CategoriaDAO:
    arquivo = "categoria.json"
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.objetos.append(obj)

    @classmethod
    def listar(cls):
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        raise IndexError("Categoria não encontrado!")

    @classmethod
    def atualizar(cls, nova_categoria):
        for i, categoria_atual in enumerate(cls.objetos):
            if nova_categoria.id == categoria_atual.id:
                cls.objetos[i] = nova_categoria
                return
        raise IndexError("Categoria não encontrado!")

    @classmethod
    def excluir(cls, id):
        for i, categoria_atual in enumerate(cls.objetos):
            if categoria_atual.id == id:
                cls.objetos.pop(i)
                return
        raise IndexError("Categoria não encontrado!")

    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open(cls.arquivo, mode="r") as arquivo:
            categorias_json = json.load(arquivo)
            for obj in categorias_json:
                c = Categoria.from_json(obj)
                cls.objetos.append(c)

    @classmethod
    def salvar(cls):
        categorias_json = [obj.to_json() for obj in cls.objetos]
        with open(cls.arquivo, mode="w") as arquivo:
            json.dump(categorias_json, arquivo)


class ProdutoDAO:
    arquivo = "produto.json"
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.objetos.append(obj)

    @classmethod
    def listar(cls):
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        raise IndexError("Produto não encontrado!")

    @classmethod
    def atualizar(cls, novo_produto):
        for i, produto_atual in enumerate(cls.objetos):
            if novo_produto.id == produto_atual.id:
                cls.objetos[i] = novo_produto
                return
        raise IndexError("Produto não encontrado!")

    @classmethod
    def excluir(cls, id):
        for i, produto_atual in enumerate(cls.objetos):
            if produto_atual.id == id:
                cls.objetos.pop(i)
                return
        raise IndexError("Produto não encontrado!")

    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open(cls.arquivo, mode="r") as arquivo:
            produtos_json = json.load(arquivo)
            for obj in produtos_json:
                p = Produto.from_json(obj)
                cls.objetos.append(p)

    @classmethod
    def salvar(cls):
        produtos_json = [obj.to_json() for obj in cls.objetos]
        with open(cls.arquivo, mode="w") as arquivo:
            json.dump(produtos_json, arquivo)


class VendaItemDAO:
    arquivo = "venda_item.json"
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.objetos.append(obj)

    @classmethod
    def listar(cls):
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        raise IndexError("Item da venda não encontrado!")

    @classmethod
    def atualizar(cls, novo_venda_item):
        for i, venda_item_atual in enumerate(cls.objetos):
            if novo_venda_item.id == venda_item_atual.id:
                cls.objetos[i] = novo_venda_item
                return
        raise IndexError("Item da venda não encontrado!")

    @classmethod
    def excluir(cls, id):
        for i, venda_item_atual in enumerate(cls.objetos):
            if venda_item_atual.id == id:
                cls.objetos.pop(i)
                return
        raise IndexError("Item da venda não encontrado!")

    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open(cls.arquivo, mode="r") as arquivo:
            venda_items_json = json.load(arquivo)
            for obj in venda_items_json:
                vi = VendaItem.from_json(obj)
                cls.objetos.append(vi)

    @classmethod
    def salvar(cls):
        venda_items_json = [obj.to_json() for obj in cls.objetos]
        with open(cls.arquivo, mode="w") as arquivo:
            json.dump(venda_items_json, arquivo)