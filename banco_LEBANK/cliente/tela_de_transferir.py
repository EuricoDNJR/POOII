from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Tela_Transferencia(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Tela_Transferencia, self).__init__(parent)
        self.settings()
        self.set_font()
        self.create_widgets()
        self.set_style()

    def settings(self):
        self.resize(800, 600)
        self.setWindowTitle("Transferencia")

    def set_font(self):
        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(16)

    def create_widgets(self):
        self.LEBANK_label = QtWidgets.QLabel("LEBANK", self)
        self.LEBANK_label.setGeometry(QtCore.QRect(0, 0, 811, 20))
        self.LEBANK_label.setFont(self.font)
        self.LEBANK_label.setAlignment(QtCore.Qt.AlignCenter)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 60, 811, 511))

        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setWeight(75)

        self.saldo_label = QtWidgets.QLabel("Saldo:", self)
        self.saldo_label.setGeometry(QtCore.QRect(580, 30, 191, 21))
        self.saldo_label.setFont(self.font)

        self.saldo_line = QtWidgets.QLineEdit(self)
        self.saldo_line.setGeometry(QtCore.QRect(630, 30, 141, 21))
        self.saldo_line.setEnabled(False)

        self.font.setBold(False)

        self.numero_da_conta_do_destinatario_label = QtWidgets.QLabel("Número da conta do destinatário:", self.frame)
        self.numero_da_conta_do_destinatario_label.setGeometry(QtCore.QRect(20, 20, 241, 31))
        self.numero_da_conta_do_destinatario_label.setFont(self.font)

        self.numero_da_conta_do_destinatario_line = QtWidgets.QLineEdit(self.frame)
        self.numero_da_conta_do_destinatario_line.setGeometry(QtCore.QRect(270, 30, 131, 20))

        self.nome_do_destinatario_label = QtWidgets.QLabel("Nome do destinatário:", self.frame)
        self.nome_do_destinatario_label.setGeometry(QtCore.QRect(10, 70, 161, 31))
        self.nome_do_destinatario_label.setFont(self.font)

        self.nome_do_destinatario_line = QtWidgets.QLineEdit(self.frame)
        self.nome_do_destinatario_line.setGeometry(QtCore.QRect(180, 80, 391, 20))
        self.nome_do_destinatario_line.setEnabled(False)

        self.voltar_botao = QtWidgets.QPushButton("Voltar", self.frame)
        self.voltar_botao.setGeometry(QtCore.QRect(470, 280, 211, 51))

        self.valor_a_ser_transferido_label = QtWidgets.QLabel("Valor à ser transferido:", self.frame)
        self.valor_a_ser_transferido_label.setGeometry(QtCore.QRect(170, 180, 161, 31))
        self.valor_a_ser_transferido_label.setFont(self.font)
        
        self.valor_a_ser_transferido_line = QtWidgets.QLineEdit(self.frame)
        self.valor_a_ser_transferido_line.setGeometry(QtCore.QRect(350, 190, 131, 20))

        self.buscar_botao = QtWidgets.QPushButton("Buscar", self.frame)
        self.buscar_botao.setGeometry(QtCore.QRect(440, 30, 81, 21))

        self.cpf_do_destinatario_label = QtWidgets.QLabel("CPF do destinatário:", self.frame)
        self.cpf_do_destinatario_label.setGeometry(QtCore.QRect(20, 130, 141, 31))
        self.cpf_do_destinatario_label.setFont(self.font)
 
        self.cpf_do_destinatario_line = QtWidgets.QLineEdit(self.frame)
        self.cpf_do_destinatario_line.setGeometry(QtCore.QRect(180, 140, 391, 20))
        self.cpf_do_destinatario_line.setEnabled(False)

        self.transferir_botao = QtWidgets.QPushButton("Transferir", self.frame)
        self.transferir_botao.setGeometry(QtCore.QRect(140, 280, 211, 51))

    def set_style(self):
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0681818 rgba(14, 8, 73, 255), stop:0.607955 rgba(28, 17, 145, 255));")
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LEBANK_label.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.210227 rgba(255, 255, 0, 255), stop:0.778409 rgba(255, 255, 117, 255));")
        self.saldo_label.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(19, 11, 98);")
        self.saldo_line.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(23, 14, 121);")
        self.numero_da_conta_do_destinatario_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nome_do_destinatario_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.voltar_botao.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.valor_a_ser_transferido_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buscar_botao.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.cpf_do_destinatario_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.transferir_botao.setStyleSheet("background-color: rgb(255, 255, 0);")


if __name__ == '__main__':
    root = QtWidgets.QApplication(sys.argv)
    app = Tela_Transferencia()
    app.show()
    sys.exit(root.exec_())
