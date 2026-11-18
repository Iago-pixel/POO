from tarefa2 import ProdutoDAO, CategoriaDAO, ClienteDAO
from tarefa1 import Produto, Categoria, Cliente


class UI:
    @classmethod
    def main(cls):
        while True:
            selecao = cls.menu()
            if selecao == 1:
                cls.cliente_listar()
            if selecao == 2:
                cls.cliente_inserir()
            if selecao == 3:
                cls.cliente_atualizar()
            if selecao == 4:
                cls.cliente_excluir()
            if selecao == 5:
                cls.categoria_listar()
            if selecao == 6:
                cls.categoria_inserir()
            if selecao == 7:
                cls.categoria_atualizar()
            if selecao == 8:
                cls.categoria_excluir()
            if selecao == 9:
                cls.produto_listar()
            if selecao == 10:
                cls.produto_inserir()
            if selecao == 11:
                cls.produto_atualizar()
            if selecao == 12:
                cls.produto_excluir()
            if selecao == 13:
                break
            input("Aperte enter para continuar...")

    @staticmethod
    def menu():
        i = 1
        for entidade in ["cliente", "categoria", "produto"]:
            print(f"{i} - Listar {entidade}s")
            i += 1
            print(f"{i} - Inserir {entidade}")
            i += 1
            print(f"{i} - Atualizar {entidade}")
            i += 1
            print(f"{i} - Excluir {entidade}")
            i += 1
        print(f"{i} - Finalizar")
        return input()

    @staticmethod
    def produto_listar():
        print("LISTA DE PRODUTOS")
        for p in ProdutoDAO().listar():
            print(p)

    @staticmethod
    def produto_inserir():
        print("INSERIR PRODUTO")
        descricao = input("Informe a descrição: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe o estoque: "))
        id_categoria = int(input("Informe o id da categoria: "))
        p = Produto(0, descricao, preco, estoque, id_categoria)
        ProdutoDAO().inserir(p)

    @staticmethod
    def produto_atualizar():
        print("ATUALIZAR PRODUTO")
        UI.produto_listar()

        id = int(input("Informe o id do produto a ser atualizado"))
        p = ProdutoDAO().listar_id(id)

        if p == None:
            print("Produto não encontrado!")
            return

        print(f"Descrição: {p.descricao}")
        while True:
            selecao = input("Deseja alterar a descrição? (y/N)")
            if selecao == "N" or selecao == "n" or selecao == "":
                descricao = p.descricao
                break
            if selecao == "y":
                descricao = input("Informe a nova descrição: ")
                break

        print(f"Preço: {p.preco}")
        while True:
            selecao = input("Deseja alterar o preço? (y/N)")
            if selecao == "N" or selecao == "n" or selecao == "":
                preco = p.preco
                break
            if selecao == "y":
                preco = float(input("Informe a novo preço: "))
                break

        print(f"Estoque: {p.estoque}")
        while True:
            selecao = input("Deseja alterar o estoque? (y/N)")
            if selecao == "N" or selecao == "n" or selecao == "":
                estoque = p.estoque
                break
            if selecao == "y":
                estoque = int(input("Informe a novo estoque: "))
                break

        print(f"Id da categoria: {p.id_categoria}")
        while True:
            selecao = input("Deseja alterar o id da categoria? (y/N)")
            if selecao == "N" or selecao == "n" or selecao == "":
                id_categoria = p.id_categoria
                break
            if selecao == "y":
                id_categoria = int(input("Informe a novo id da categoria: "))
                break

        p_atualizado = Produto(id, descricao, preco, estoque, id_categoria)
        ProdutoDAO().atualizar(p_atualizado)

    @staticmethod
    def produto_excluir():
        print("EXCLUIR PRODUTO")
        UI.produto_listar()
        id = int(input("Informe o id do produto ser excluído: "))
        ProdutoDAO().excluir(id)

    @staticmethod
    def categoria_listar():
        print("LISTA DE CATEGORIA")
        for c in CategoriaDAO().listar():
            print(c)

    @staticmethod
    def categoria_inserir():
        print("INSERIR CATEGORIA")
        descricao = input("Informe a descrição: ")
        c = Categoria(0, descricao)
        CategoriaDAO().inserir(c)

    @staticmethod
    def categoria_atualizar():
        print("ATUALIZAR CATEGORIA")
        UI.categoria_listar()

        id = int(input("Informe o id da categoria a ser atualizado"))
        c = CategoriaDAO().listar_id(id)

        if c == None:
            print("Categoria não encontrada!")
            return

        print(f"Descrição: {c.descricao}")
        while True:
            selecao = input("Deseja alterar a descrição? (y/N)")
            if selecao == "N" or selecao == "n" or selecao == "":
                descricao = c.descricao
                break
            if selecao == "y":
                descricao = input("Informe a nova descrição: ")
                break

        c_atualizado = Categoria(id, descricao)
        CategoriaDAO().atualizar(c_atualizado)

    @staticmethod
    def categoria_excluir():
        print("EXCLUIR CATEGORIA")
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser excluído: "))
        CategoriaDAO().excluir(id)

    @staticmethod
    def cliente_listar():
        print("LISTA DE CLIENTES")
        for c in ClienteDAO().listar():
            print(c)

    @staticmethod
    def cliente_inserir():
        print("INSERIR CLIENTE")
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        c = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(c)

    @staticmethod
    def cliente_atualizar():
        print("ATUALIZAR CLIENTE")
        UI.cliente_listar()

        id = int(input("Informe o id do cliente a ser atualizado"))
        c = ClienteDAO().listar_id(id)

        if c == None:
            print("Cliente não encontrada!")
            return

        print(f"Nome: {c.nome}")
        while True:
            selecao = input("Deseja alterar o nome? (y/N)")
            if selecao == "N" or selecao == "n" or selecao == "":
                nome = c.nome
                break
            if selecao == "y":
                nome = input("Informe o novo nome: ")
                break

        print(f"E-mail: {c.email}")
        while True:
            selecao = input("Deseja alterar o e-mail? (y/N)")
            if selecao == "N" or selecao == "n" or selecao == "":
                email = c.email
                break
            if selecao == "y":
                email = input("Informe o novo e-mail: ")
                break

        print(f"Telefone: {c.fone}")
        while True:
            selecao = input("Deseja alterar o telefone? (y/N)")
            if selecao == "N" or selecao == "n" or selecao == "":
                fone = c.fone
                break
            if selecao == "y":
                fone = input("Informe o novo telefone: ")
                break

        c_atualizado = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(c_atualizado)

    @staticmethod
    def cliente_excluir():
        print("EXCLUIR CLIENTE")
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        ClienteDAO().excluir(id)