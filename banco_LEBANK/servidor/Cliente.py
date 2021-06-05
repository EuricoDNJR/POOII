class Cliente():
    """
    
    Classe responsavel pela criação do cliente.

    :ivar self._nome: Nome do cliente
    :vartype self._nome: str
    :ivar self._sobrenome: Resto do nome do cliente
    :vartype self._sobrenome: str
    :ivar self._cpf: CPF do cliente
    :vartype self._cpf: str

    """
    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        
    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
    	return self._sobrenome
    

    @property
    def cpf(self):
        return self._cpf
