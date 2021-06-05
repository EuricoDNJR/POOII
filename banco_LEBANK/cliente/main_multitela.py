import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from tela_inicial import Tela_Inicial
from tela_de_cadastro import Tela_Cadastro
from tela_de_depositar import Tela_Deposito
from tela_de_extrato import Tela_Extrato
from tela_de_login import Tela_Login
from tela_de_saque import Tela_Saque
from tela_de_transferir import Tela_Transferencia
from tela_principal import Tela_Principal

from socket import socket, AF_INET, SOCK_STREAM


class Main(QtWidgets.QStackedLayout):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.tela_inicial = Tela_Inicial()
        self.tela_cadastro = Tela_Cadastro()
        self.tela_depositar = Tela_Deposito()
        self.tela_extrato = Tela_Extrato()
        self.tela_login = Tela_Login()
        self.tela_saque = Tela_Saque()
        self.tela_transferir = Tela_Transferencia()
        self.tela_principal = Tela_Principal()

        self.addWidget(self.tela_inicial)
        self.addWidget(self.tela_cadastro)
        self.addWidget(self.tela_depositar)
        self.addWidget(self.tela_extrato)
        self.addWidget(self.tela_login)
        self.addWidget(self.tela_saque)
        self.addWidget(self.tela_transferir)
        self.addWidget(self.tela_principal)

        self.set_connects()
        self.connect_server()

        self.conta = None

    def set_connects(self):
        self.tela_inicial.cadastrar_se_botao.clicked.connect(self.cadastrarAbrirTela)
        self.tela_inicial.login_botao.clicked.connect(self.loginAbrirTela)

        self.tela_cadastro.confirmar_botao.clicked.connect(self.cadastrarCliente)
        self.tela_cadastro.voltar_botao.clicked.connect(self.voltarTelaInicial)

        self.tela_login.logar_botao.clicked.connect(self.logarCliente)
        self.tela_login.voltar_botao.clicked.connect(self.voltarTelaInicial)

        self.tela_principal.sair_botao.clicked.connect(self.sairTelaPrincipal)
        self.tela_principal.ver_extrato_botao.clicked.connect(self.extratoAbrirTela)
        self.tela_principal.transferir_botao.clicked.connect(self.transferirAbrirTela)
        self.tela_principal.sacar_botao.clicked.connect(self.sacarAbrirTela)
        self.tela_principal.depositar_botao.clicked.connect(self.depositarAbrirTela)

        self.tela_extrato.voltar_botao.clicked.connect(self.entrarTelaPrincipal)
        self.tela_transferir.voltar_botao.clicked.connect(self.entrarTelaPrincipal)
        self.tela_saque.voltar_botao.clicked.connect(self.entrarTelaPrincipal)
        self.tela_depositar.voltar_botao.clicked.connect(self.entrarTelaPrincipal)

        self.tela_saque.confirmar_botao.clicked.connect(self.saqueConfirmar)
        self.tela_depositar.confirmar_botao.clicked.connect(self.depositoConfirmar)

        self.tela_transferir.transferir_botao.clicked.connect(self.transferirSaldo)
        self.tela_transferir.buscar_botao.clicked.connect(self.buscarDestinatario)

    def connect_server(self):
        self.ip = 'localhost'
        self.port = 8000
        self.address = ((self.ip, self.port))

        self.cliente_socket = socket(AF_INET, SOCK_STREAM)
        self.cliente_socket.connect(self.address)

    def cadastrarAbrirTela(self):
        self.tela_cadastro.nome_line.setText('')
        self.tela_cadastro.sobrenome_line.setText('')
        self.tela_cadastro.cpf_line.setText('')
        self.tela_cadastro.senha_line.setText('')

        self.setCurrentIndex(1)

    def requestEnviar(self, request):
        '''

        Envia ao servidor uma solicitação de serviço juntamente com as informações necessárias para a execução
        da mesma, e aguarda a resposta.


        :param request: A solicitação a ser enviada
        :type request: str
        :ivar resposta: A resposta da requisição feita

        :returns: A resposta da requisição feita em forma de lista sendo a "," o separador.
        :rtype: list
        
        '''
        self.cliente_socket.send(request.encode())

        resposta = self.cliente_socket.recv(1024).decode()

        return resposta.split(",")

    def loginAbrirTela(self):
        self.setCurrentIndex(4)
        self.conta = None

    def cadastrarCliente(self):
        nome = self.tela_cadastro.nome_line.text()
        sobrenome = self.tela_cadastro.sobrenome_line.text()
        cpf = self.tela_cadastro.cpf_line.text()
        senha = self.tela_cadastro.senha_line.text()

        if nome != '' and sobrenome != '' and cpf != '' and senha != '':

            resposta = self.requestEnviar("cadastrar_cliente" + "," + nome + "," + sobrenome + "," + cpf + "," + senha)

            if resposta[0] == "True":

                QMessageBox.information(None, "LEBANK",
                                        f"Cadastro feito com sucesso\n\nNumero da conta: " + resposta[1])
                self.voltarTelaInicial()

            else:
                QMessageBox.information(None, "LEBANK", "Falha ao cadastrar dados do cliente")

        else:
            QMessageBox.information(None, "LEBANK", "Preencha todos os campos")

    def voltarTelaInicial(self):
        self.setCurrentIndex(0)

    def logarCliente(self):
        numero_da_conta = self.tela_login.numero_da_conta_line.text()
        senha = self.tela_login.senha_line.text()

        if numero_da_conta != '' and senha != '':
            resposta = self.requestEnviar("login" + "," + numero_da_conta + "," + senha)

            if resposta[0] == "True":
                self.conta = {"numero_da_conta": numero_da_conta, "senha": senha}
                self.tela_login.numero_da_conta_line.setText('')
                self.tela_login.senha_line.setText('')
                self.entrarTelaPrincipal()
            else:
                QMessageBox.information(None, "LEBANK", "Falha no login")
        else:
            QMessageBox.information(None, "LEBANK", "Preencha todos os campos")

    def entrarTelaPrincipal(self):
        self.setCurrentIndex(7)

        resposta = self.requestEnviar("get_titular" + "," + self.conta["numero_da_conta"] + "," + self.conta["senha"])

        if resposta[0] == "True":
            self.tela_principal.titular_line.setText(resposta[1])

        resposta = self.requestEnviar("get_saldo" + "," + self.conta["numero_da_conta"] + "," + self.conta["senha"])

        if resposta[0] == "True":
            self.tela_principal.saldo_line.setText(resposta[1])

    def sairTelaPrincipal(self):
        self.setCurrentIndex(4)

    def extratoAbrirTela(self):
        self.setCurrentIndex(3)

        resposta_titular = self.requestEnviar(
            "get_titular" + "," + self.conta["numero_da_conta"] + "," + self.conta["senha"])

        resposta_saldo = self.requestEnviar(
            "get_saldo" + "," + self.conta["numero_da_conta"] + "," + self.conta["senha"])

        resposta_limite = self.requestEnviar(
            "get_limite" + "," + self.conta["numero_da_conta"] + "," + self.conta["senha"])

        resposta_historico = self.requestEnviar(
            "get_historico" + "," + self.conta["numero_da_conta"] + "," + self.conta["senha"])

        self.tela_extrato.numero_line.setText(self.conta["numero_da_conta"])

        if resposta_titular[0] == "True":
            self.tela_extrato.titular_line.setText(resposta_titular[1])

        if resposta_saldo[0] == "True":
            self.tela_extrato.saldo_line.setText(resposta_saldo[1])

        if resposta_limite[0] == "True":
            self.tela_extrato.limite_line.setText(resposta_limite[1])

        if resposta_historico[0] == "True":
            self.tela_extrato.historico_line.setText(resposta_historico[1])

    def transferirAbrirTela(self):
        self.setCurrentIndex(6)

        resposta = self.requestEnviar("get_saldo" + "," + self.conta["numero_da_conta"] + "," + self.conta["senha"])

        if resposta[0] == "True":
            self.tela_transferir.saldo_line.setText(resposta[1])

        self.tela_transferir.numero_da_conta_do_destinatario_line.setText('')
        self.tela_transferir.nome_do_destinatario_line.setText('')
        self.tela_transferir.cpf_do_destinatario_line.setText('')
        self.tela_transferir.valor_a_ser_transferido_line.setText('')

    def sacarAbrirTela(self):
        self.setCurrentIndex(5)

        self.tela_saque.valor_a_ser_sacado_line.setText('')

        resposta = self.requestEnviar("get_saldo" + "," + self.conta["numero_da_conta"] + "," + self.conta["senha"])

        if resposta[0] == "True":
            self.tela_saque.saldo_line.setText(resposta[1])

    def saqueConfirmar(self):
        valor_a_ser_sacado = self.tela_saque.valor_a_ser_sacado_line.text()

        try:
            if valor_a_ser_sacado != '':
                resposta = self.requestEnviar("sacar" + "," + self.conta["numero_da_conta"] + "," + self.conta[
                    "senha"] + "," + valor_a_ser_sacado.replace(',', '.'))

                if resposta[0] == "True":
                    QMessageBox.information(None, "LEBANK", "Saque realizado com sucesso")
                    self.entrarTelaPrincipal()
                else:
                    QMessageBox.information(None, "LEBANK", "Valor invalido\nou\nMaior que o saldo")
            else:
                QMessageBox.information(None, "LEBANK", "Preencha o campo")
        except:
            QMessageBox.information(None, "LEBANK", "Ocorreu um erro")

    def depositarAbrirTela(self):

        resposta = self.requestEnviar("get_saldo" + "," + self.conta["numero_da_conta"] + "," + self.conta["senha"])

        if resposta[0] == "True":
            self.tela_depositar.saldo_line.setText(resposta[1])

        self.tela_depositar.valor_a_ser_depositado_line.setText('')

        self.setCurrentIndex(2)

    def depositoConfirmar(self):
        valor_a_ser_depositado = self.tela_depositar.valor_a_ser_depositado_line.text()

        try:
            if valor_a_ser_depositado != '':
                resposta = self.requestEnviar("depositar" + "," + self.conta["numero_da_conta"] + "," + self.conta[
                    "senha"] + "," + valor_a_ser_depositado.replace(',', '.'))

                if resposta[0] == "True":
                    QMessageBox.information(None, "LEBANK", "Deposito realizado com sucesso")
                    self.entrarTelaPrincipal()
                else:
                    QMessageBox.information(None, "LEBANK", "Valor invalido\nou\nPassa do limite")
            else:
                QMessageBox.information(None, "LEBANK", "Preencha o campo")
        except:
            QMessageBox.information(None, "LEBANK", "Ocorreu um erro")

    def transferirSaldo(self):
        numero_da_conta_do_destinatario = self.tela_transferir.numero_da_conta_do_destinatario_line.text()
        valor_a_ser_transferido = self.tela_transferir.valor_a_ser_transferido_line.text()

        try:
            if numero_da_conta_do_destinatario != '' and valor_a_ser_transferido != '':

                resposta = self.requestEnviar("transferir" + "," + self.conta["numero_da_conta"] + "," + self.conta[
                    "senha"] + "," + numero_da_conta_do_destinatario + "," + valor_a_ser_transferido.replace(',', '.'))

                if resposta[0] == "True":
                    QMessageBox.information(None, "LEBANK", "Transferencia realizada com sucesso\n")
                    self.entrarTelaPrincipal()
                else:
                    QMessageBox.information(None, "LEBANK", "Valor invalido")
            else:
                QMessageBox.information(None, "LEBANK", "Preencha os campos necessarios")
        except:
            QMessageBox.information(None, "LEBANK", "Ocorreu um erro")

    def buscarDestinatario(self):
        numero_da_conta_do_destinatario = self.tela_transferir.numero_da_conta_do_destinatario_line.text()

        resposta = self.requestEnviar(
            "get_titular_cpf_destinatario" + "," + self.conta["numero_da_conta"] + "," + self.conta[
                "senha"] + "," + numero_da_conta_do_destinatario)

        try:
            if numero_da_conta_do_destinatario != '':
                if resposta[0] == "True":
                    self.tela_transferir.nome_do_destinatario_line.setText(resposta[1])
                    self.tela_transferir.cpf_do_destinatario_line.setText(resposta[2] + '********')
                else:
                    QMessageBox.information(None, "LEBANK", "Destinatário não encontrado")
                    self.tela_transferir.nome_do_destinatario_line.setText('')
                    self.tela_transferir.cpf_do_destinatario_line.setText('')
            else:
                QMessageBox.information(None, "LEBANK", "Informe o numero da conta do destinatario")
                self.tela_transferir.nome_do_destinatario_line.setText('')
                self.tela_transferir.cpf_do_destinatario_line.setText('')
        except:
            QMessageBox.information(None, "LEBANK", "Ocorreu um erro")
            self.tela_transferir.nome_do_destinatario_line.setText('')
            self.tela_transferir.cpf_do_destinatario_line.setText('')


if __name__ == '__main__':
    root = QtWidgets.QApplication(sys.argv)
    app = Main()
    sys.exit(root.exec_())
