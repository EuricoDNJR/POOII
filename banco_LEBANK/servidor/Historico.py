class Historico():
    """
    
    Classe responsável por gerenciar o histórico das contas.

    :ivar self._transacoes: Armazena as transações.
    :vartype self._transacoes: list

    """
    def __init__(self):
        self._transacoes = []
        
    def add_transacao(self, transacao, valor):
        """

        Adiciona a transação.

        :ivar transacao: Transação a ser adicionada
        :vartype transacao: str
        :ivar valor: Valor da transação
        :vartype valor: float

        :return: Retorna True se ocorreu, e False se não.
        :rtype: bool

        """
        try:
            self._transacoes.append(transacao + '  ' + str(valor) + '\n\n')
            return True
        except:
            return False

    @property
    def transacoes(self):
        return self._transacoes
