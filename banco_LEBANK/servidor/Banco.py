from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from Conta import Conta
from Cliente import Cliente


class Banco:
	"""

	O objeto Banco contém os metódos necessários para o processamento e armazenamento das informações requisitadas.
	
	:ivar self._clientes: Usado para armazenar os clientes em um dicionario onde a key é seu CPF
	:vartype self._clientes: dict
	:ivar self._contas: Usado para armazenar as contas em um dicionario onde a key é o numero da conta
	:vartype self._contas: dict
	:ivar self.requests: Usado para armazenar os requests em um dicionario onde a key é o request
	:vartype self.requests: dict

	"""
	def __init__(self):
		self._clientes = {}
		self._contas = {}
		self.requests = {}
		self.create_requests()
		self.create_server()
		self.start_server()

	@property
	def clientes(self):
		return self._clientes

	@property
	def contas(self):
		return self._contas

	def create_server(self):
		self.host = 'localhost'
		self.port = 8000
		self.address = (self.host, self.port)

		self.server_socket = socket(AF_INET, SOCK_STREAM)
		self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		self.server_socket.bind(self.address)
		self.server_socket.listen(10)

	def adicionar_request(self, request_name, request_func):
		"""

		Adiciona ao dicionario de request o nome e a função do respectivo request(instrução).

		:param request_name: Nome do request
		:type request_name: str
		:param request_func: Função do request
		:type request_func: func

		"""
		self.requests[request_name] = request_func

	def create_requests(self):
		self.adicionar_request("cadastrar_cliente", self.cadastrarCliente)
		self.adicionar_request("login", self.login)
		self.adicionar_request("get_titular", self.getTitular)
		self.adicionar_request("get_saldo", self.getSaldo)
		self.adicionar_request("get_limite", self.getLimite)
		self.adicionar_request("get_historico", self.getHistorico)
		self.adicionar_request("get_titular_cpf_destinatario", self.getTitularCpfDestinatario)
		self.adicionar_request("sacar", self.sacar)
		self.adicionar_request("depositar", self.depositar)
		self.adicionar_request("transferir", self.transferir)

	def requestReceber(self):
		"""

		Recebe o request enviado pelo cliente decodifica ele, e depois transforma em lista
		sendo o separador a ",".

		:ivar request: Mensagem decodificada
		:vartype request: str
		:ivar request_list: Mensagem em formato de lista
		:vartype request_list: list

		:return: O primeiro indice(o nome da função do request) e seus parametros necessarios para a realização da mesmo)

		"""
		request = self.con.recv(1024).decode()

		request_list = request.split(",")

		return request_list[0], request_list[1:]

	def start_server(self):
		"""
		
		Inicia o servidor, aguarda a conexão, e responde os requests.

		:ivar request_name: Recebe o nome do request
		:vartype request_name: str
		:ivar request_parameters: Recebe os parametros necessário para o determinado request
		:vartype request_parameters: list
		:ivar func: Recebe a função do request
		:vartype resposta: Recebe a resposta da função requisitada
		:return: A resposta

		"""
		print("START SERVER...")

		self.con, self.cliente = self.server_socket.accept()

		while(True):
			request_name, request_parameters = self.requestReceber()

			try:
				func = self.requests[request_name]

				resposta = func(request_parameters)
			except:
				break

			self.con.send(resposta.encode())

		self.server_socket.close()

	def cadastrarCliente(self, request_parameters):
		"""

		Cria o cliente mas so o adiciona na lista de clientes quando é verificado a existencia de seu
		CPF na lista, se seu cpf é numerico e se tem 11 digitos. Apos isso conta do cliente é cadastrada juntamente
		com a senha colocada.Por fim retorna True se deu certo juntamente com a quantidade de contas criadas. 
		
		"""
		print("Cadastrando cliente")

		resposta = 'False'

		cliente = Cliente(request_parameters[0], request_parameters[1], request_parameters[2])

		if cliente.cpf not in self.clientes and cliente.cpf.isdigit() and len(cliente.cpf) == 11:
			self.clientes[cliente.cpf] = cliente

			if self.cadastrarConta(Conta(cliente, request_parameters[3])):
				resposta = "True"
				resposta += ","
				resposta += str(Conta.qtd_de_contas())

		return resposta

	def cadastrarConta(self, conta):
		"""

		Adiciona a conta ao dicionario de contas, sendo a key o numero da conta.
		
		:param conta: A respectiva conta do cliente
		:type conta: Conta Object
		:return: True se funcionar
		:rtype: bool
		
		"""
		print("Cadastrando conta")

		self.contas[conta.numero] = conta
		return True

	def login(self, request_parameters):
		"""

		Verifica o login da conta por meio da sua senha cadastrada.
		
		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta e o segundo a senha.
		:type request_parameters: list
		:return: Retorna True se a senha coincidir e False se não.
		:rtype: str

		"""
		print("Verificando login")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = "True"

		return resposta

	def getTitular(self, request_parameters):
		"""

		Retorna o nome e o sobrenome do titular da conta por meio do numero da conta.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta e o segundo a senha.
		:return: Se der tudo certo True é retornado, juntamente com as informações requisitadas, divididas por virgula.
		:rtype: str

		"""
		print("Buscando e retornando titular")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = "True"
			resposta += ','
			resposta += self.contas[request_parameters[0]].titular.nome
			resposta += ' '
			resposta += self.contas[request_parameters[0]].titular.sobrenome

		return resposta

	def getSaldo(self, request_parameters):
		"""

		Retorna o saldo da conta por meio do numero.
		
		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta e o segundo a senha.
		:return: Se der tudo certo True é retornado, juntamente com as informações requisitadas, divididas por virgula.
		:rtype: str

		"""
		print("Buscando e retornando saldo")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = "True"
			resposta += ','
			resposta += str(self.contas[request_parameters[0]].saldo)

		return resposta

	def getLimite(self, request_parameters):
		"""

		Retorna o limite da conta por meio do numero.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta e o segundo a senha.
		:return: Se der tudo certo True é retornado, juntamente com as informações requisitadas, divididas por virgula.
		:rtype: str

		"""
		print("Buscando e retornando limite")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = 'True'
			resposta += ','
			resposta += str(self.contas[request_parameters[0]].limite)

		return resposta

	def getHistorico(self, request_parameters):
		"""

		Retorna o historico da conta por meio do numero.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta e o segundo a senha.
		:return: Se der tudo certo True é retornado, juntamente com as informações requisitadas, divididas por virgula.
		:rtype: str
		
		"""
		print("Buscando e retornando historico")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = "True"
			resposta += ","
			resposta += self.contas[request_parameters[0]].extrato()

		return resposta

	def getTitularCpfDestinatario(self, request_parameters):
		"""

		Retorna o nome, sobrenome e cpf da conta do destinatário por meio do numero.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta,o segundo a senha, o terceiro o numero da conta do destinatário.
		:return: Se der tudo certo True é retornado, juntamente com as informações requisitadas, divididas por virgula.
		:rtype: str
		
		"""
		print("Buscando e retornando titular e cpf do destinatario")

		resposta = "False"

		try:
			if self.contas[request_parameters[0]].senha == request_parameters[1]:
				resposta = "True"
				resposta += ","
				resposta += self.contas[request_parameters[2]].titular.nome
				resposta += ' '
				resposta += self.contas[request_parameters[2]].titular.sobrenome
				resposta += ','
				resposta += self.contas[request_parameters[2]].titular.cpf[0:3]
		except:
			pass

		return resposta

	def sacar(self, request_parameters):
		"""

		Realiza o saque da conta por meio do metodo saca da classe Conta, passando o valor a ser retirado.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta, o segundo a senha, o terceiro o valor a ser sacado.
		:return: Se der tudo certo True é retornado.
		:rtype: str
		
		"""

		print("Realizando saque")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = str(self.contas[request_parameters[0]].saca(float(request_parameters[2])))

		return resposta

	def depositar(self, request_parameters):
		"""

		Realiza o deposito na conta por meio do metodo deposita da classe Conta, passando o valor a ser depositado.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta, o segundo a senha, o terceiro o valor a ser depositado.
		:return: Se der tudo certo True é retornado.
		:rtype: str
		
		"""
		print("Realizando deposito")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = str(self.contas[request_parameters[0]].deposita(float(request_parameters[2])))

		return resposta

	def transferir(self, request_parameters):
		"""

		Realiza a transferencia para a conta por meio do metodo transfere da classe Conta, passando o valor a ser transferido.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta, o segundo a senha, sendo o terceiro e quarto, o numero da conta do destinatário e o valor a ser transferido.
		:return: Se der tudo certo True é retornado.
		:rtype: str
		
		"""

		print("Realizando transferencia")

		resposta = "False"
		try:
			if self.contas[request_parameters[0]].senha == request_parameters[1]:
				resposta = str(self.contas[request_parameters[0]].transfere(self.contas[request_parameters[2]], float(request_parameters[3])))
		except:
			pass

		return resposta


if __name__ == "__main__":
	banco = Banco()
