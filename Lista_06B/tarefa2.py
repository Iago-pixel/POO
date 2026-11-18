import json
from tarefa1 import Cliente, Venda, Categoria, Produto, VendaItem


class ClienteDAO:
    def __init__(self):
        self.__arquivo = "cliente.json"
        self.__objetos = []

    def inserir(self, obj):
        self.__abrir()
        id = 0
        if len(self.__objetos) != 0:
            id = max(self.__objetos, key = lambda x : x.id).id
        obj.id = id + 1    
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        self.__abrir()
        return self.__objetos

    def listar_id(self, id):
        self.__abrir()
        for obj in self.__objetos:
            if obj.id == id:
                return obj
        return None

    def atualizar(self, novo_cliente):
        self.__abrir()
        for i, cliente_atual in enumerate(self.__objetos):
            if novo_cliente.id == cliente_atual.id:
                self.__objetos[i] = novo_cliente
                self.__salvar()
                return

    def excluir(self, id):
        self.__abrir()
        for i, cliente_atual in enumerate(self.__objetos):
            if cliente_atual.id == id:
                self.__objetos.pop(i)
                self.__salvar()
                return

    def __abrir(self):
        self.__objetos = []
        with open(self.__arquivo, mode="r") as arquivo:
            clientes_json = json.load(arquivo)
            for obj in clientes_json:
                c = Cliente.from_json(obj)
                self.__objetos.append(c)

    def __salvar(self):
        clientes_json = [obj.to_json() for obj in self.__objetos]
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump(clientes_json, arquivo, indent = 2)


class VendaDAO:
    def __init__(self):
        self.__arquivo = "venda.json"
        self.__objetos = []

    def inserir(self, obj):
        self.__abrir()
        id = 0
        if len(self.__objetos) != 0:
            id = max(self.__objetos, key = lambda x : x.id).id
        obj.id = id + 1
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        self.__abrir()
        return self.__objetos

    def listar_id(self, id):
        self.__abrir()
        for obj in self.__objetos:
            if obj.id == id:
                return obj
        return None

    def atualizar(self, nova_venda):
        self.__abrir()
        for i, venda_atual in enumerate(self.__objetos):
            if nova_venda.id == venda_atual.id:
                self.__objetos[i] = nova_venda
                self.__salvar()
                return

    def excluir(self, id):
        self.__abrir()
        for i, venda_atual in enumerate(self.__objetos):
            if venda_atual.id == id:
                self.__objetos.pop(i)
                self.__salvar()
                return

    def __abrir(self):
        self.__objetos = []
        with open(self.__arquivo, mode="r") as arquivo:
            vendas_json = json.load(arquivo)
            for obj in vendas_json:
                v = Venda.from_json(obj)
                self.__objetos.append(v)

    def __salvar(self):
        vendas_json = [obj.to_json() for obj in self.__objetos]
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump(vendas_json, arquivo, indent = 2)


class CategoriaDAO:
    def __init__(self):
        self.__arquivo = "categoria.json"
        self.__objetos = []

    def inserir(self, obj):
        self.__abrir()
        id = 0
        if len(self.__objetos) != 0:
            id = max(self.__objetos, key = lambda x : x.id).id
        obj.id = id + 1    
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        self.__abrir()
        return self.__objetos

    def listar_id(self, id):
        self.__abrir()
        for obj in self.__objetos:
            if obj.id == id:
                return obj
        return None

    def atualizar(self, nova_categoria):
        self.__abrir()
        for i, categoria_atual in enumerate(self.__objetos):
            if nova_categoria.id == categoria_atual.id:
                self.__objetos[i] = nova_categoria
                self.__salvar()
                return

    def excluir(self, id):
        self.__abrir()
        for i, categoria_atual in enumerate(self.__objetos):
            if categoria_atual.id == id:
                self.__objetos.pop(i)
                self.__salvar()
                return

    def __abrir(self):
        self.__objetos = []
        with open(self.__arquivo, mode="r") as arquivo:
            categorias_json = json.load(arquivo)
            for obj in categorias_json:
                c = Categoria.from_json(obj)
                self.__objetos.append(c)

    def __salvar(self):
        categorias_json = [obj.to_json() for obj in self.__objetos]
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump(categorias_json, arquivo, indent = 2)


class ProdutoDAO:
    def __init__(self):
        self.__arquivo = "produto.json"
        self.__objetos = []

    def inserir(self, obj):
        self.__abrir()
        id = 0
        if len(self.__objetos) != 0:
            id = max(self.__objetos, key = lambda x : x.id).id
        obj.id = id + 1    
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        self.__abrir()
        return self.__objetos

    def listar_id(self, id):
        self.__abrir()
        for obj in self.__objetos:
            if obj.id == id:
                return obj
        return None

    def atualizar(self, novo_produto):
        self.__abrir()
        for i, produto_atual in enumerate(self.__objetos):
            if novo_produto.id == produto_atual.id:
                self.__objetos[i] = novo_produto
                self.__salvar()
                return

    def excluir(self, id):
        self.__abrir()
        for i, produto_atual in enumerate(self.__objetos):
            if produto_atual.id == id:
                self.__objetos.pop(i)
                self.__salvar()
                return

    def __abrir(self):
        self.__objetos = []
        with open(self.__arquivo, mode="r") as arquivo:
            produtos_json = json.load(arquivo)
            for obj in produtos_json:
                p = Produto.from_json(obj)
                self.__objetos.append(p)

    def __salvar(self):
        produtos_json = [obj.to_json() for obj in self.__objetos]
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump(produtos_json, arquivo, indent = 2)


class VendaItemDAO:
    def __init__(self):
        self.__arquivo = "venda_item.json"
        self.__objetos = []

    def inserir(self, obj):
        self.__abrir()
        id = 0
        if len(self.__objetos) != 0:
            id = max(self.__objetos, key = lambda x : x.id).id
        obj.id = id + 1
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        self.__abrir()
        return self.__objetos

    def listar_id(self, id):
        self.__abrir()
        for obj in self.__objetos:
            if obj.id == id:
                return obj
        return None

    def atualizar(self, novo_venda_item):
        self.__abrir()
        for i, venda_item_atual in enumerate(self.__objetos):
            if novo_venda_item.id == venda_item_atual.id:
                self.__objetos[i] = novo_venda_item
                self.__salvar()
                return

    def excluir(self, id):
        self.__abrir()
        for i, venda_item_atual in enumerate(self.__objetos):
            if venda_item_atual.id == id:
                self.__objetos.pop(i)
                self.__salvar()
                return

    def __abrir(self):
        self.__objetos = []
        with open(self.__arquivo, mode="r") as arquivo:
            venda_items_json = json.load(arquivo)
            for obj in venda_items_json:
                vi = VendaItem.from_json(obj)
                self.__objetos.append(vi)

    def __salvar(self):
        venda_items_json = [obj.to_json() for obj in self.__objetos]
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump(venda_items_json, arquivo, indent = 2)