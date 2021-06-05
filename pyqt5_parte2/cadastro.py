class Cadastro:
    __slots__ = ['_lista_pessoas']

    def __init__(self):
        self._lista_pessoas = []

    def cadastra(self, pessoa):
        existe = self.busca(pessoa.cpf)
        if existe is None:
            self._lista_pessoas.append(pessoa)
            return True
        else:
            return False

    def busca(self, cpf):
        for lp in self._lista_pessoas:
            if lp.cpf == cpf:
                return lp
        return None
