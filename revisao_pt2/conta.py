import datetime


class Conta:
    _total_contas = 0
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico']

    def __init__(self, numero, cliente, limite=1000.0):
        self._numero = numero
        self._titular = cliente
        self._saldo = 0.0
        self._limite = limite
        self._historico = Historico()
        Conta._total_contas += 1

    @staticmethod
    def get_total_contas():
        return Conta._total_contas

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self, historico):
        self._historico = historico

    def deposita(self, valor):
        self._saldo += valor
        self._historico.transacoes.append("deposito de {}".format(valor))

    def saca(self, valor):
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            self._historico.transacoes.append("saque de {}".format(valor))
            return True

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if not retirou:
            return False
        else:
            destino.deposita(valor)
            self._historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
            return True

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
        self._historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))


class Cliente:
    __slots__ = ['_nome', '_sobrenome', '_cpf']

    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("data abertura: {}".format(self.data_abertura))
        print("transações: ")
        for t in self.transacoes:
            print("-", t)
