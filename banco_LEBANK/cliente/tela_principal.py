from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Tela_Principal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Tela_Principal, self).__init__(parent)
        self.settings()
        self.set_font()
        self.create_widgets()
        self.set_style()

    def settings(self):
        self.resize(800, 600)
        self.setWindowTitle("Principal")

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
        self.frame.setGeometry(QtCore.QRect(-10, 60, 811, 451))

        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setWeight(75)

        self.saldo_label = QtWidgets.QLabel("Saldo:", self)
        self.saldo_label.setGeometry(QtCore.QRect(580, 30, 191, 21))
        self.saldo_label.setFont(self.font)

        self.saldo_line = QtWidgets.QLineEdit(self)
        self.saldo_line.setGeometry(QtCore.QRect(630, 30, 141, 21))
        self.saldo_line.setEnabled(False)

        self.titular_label = QtWidgets.QLabel("Titular:", self)
        self.titular_label.setGeometry(QtCore.QRect(10, 30, 341, 21))
        self.titular_label.setFont(self.font)

        self.titular_line = QtWidgets.QLineEdit(self)
        self.titular_line.setGeometry(QtCore.QRect(70, 30, 281, 21))
        self.titular_line.setEnabled(False)

        self.font.setFamily("Impact")
        self.font.setBold(False)
        self.font.setWeight(50)

        self.ver_extrato_botao = QtWidgets.QPushButton("Ver extrato", self.frame)
        self.ver_extrato_botao.setGeometry(QtCore.QRect(150, 30, 171, 121))
        self.ver_extrato_botao.setFont(self.font)

        self.transferir_botao = QtWidgets.QPushButton("Transferir", self.frame)
        self.transferir_botao.setGeometry(QtCore.QRect(530, 30, 171, 121))
        self.transferir_botao.setFont(self.font)

        self.sacar_botao = QtWidgets.QPushButton("Sacar", self.frame)
        self.sacar_botao.setGeometry(QtCore.QRect(150, 220, 171, 121))
        self.sacar_botao.setFont(self.font)

        self.depositar_botao = QtWidgets.QPushButton("Depositar", self.frame)
        self.depositar_botao.setGeometry(QtCore.QRect(530, 220, 171, 121))
        self.depositar_botao.setFont(self.font)

        self.sair_botao = QtWidgets.QPushButton("Sair", self.frame)
        self.sair_botao.setGeometry(QtCore.QRect(350, 370, 171, 61))
        self.sair_botao.setFont(self.font)

    def set_style(self):
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0681818 rgba(14, 8, 73, 255), stop:0.607955 rgba(28, 17, 145, 255));")
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0681818 rgba(14, 8, 73, 255), stop:0.607955 rgba(28, 17, 145, 255));")
        self.LEBANK_label.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.210227 rgba(255, 255, 0, 255), stop:0.778409 rgba(255, 255, 117, 255));")
        self.saldo_label.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(19, 11, 98);")
        self.saldo_line.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(23, 14, 121);")
        self.titular_label.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(19, 11, 98);")
        self.titular_line.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(23, 14, 121);")
        self.ver_extrato_botao.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145);")
        self.transferir_botao.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145);")
        self.sacar_botao.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145);")
        self.depositar_botao.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145);")
        self.sair_botao.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145);")



if __name__ == '__main__':
    root = QtWidgets.QApplication(sys.argv)
    app = Tela_Principal()
    app.show()
    sys.exit(root.exec_())
