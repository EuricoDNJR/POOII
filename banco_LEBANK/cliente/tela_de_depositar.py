from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Tela_Deposito(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Tela_Deposito, self).__init__(parent)
        self.settings()
        self.set_font()
        self.create_widgets()
        self.set_style()

    def settings(self):
        self.resize(800, 600)
        self.setWindowTitle("Deposito")

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
        self.frame.setGeometry(QtCore.QRect(0, 100, 811, 271))

        self.font.setPointSize(12)

        self.valor_a_ser_depositado_label = QtWidgets.QLabel("Valor à ser depositado:", self.frame)
        self.valor_a_ser_depositado_label.setGeometry(QtCore.QRect(110, 60, 161, 31))
        self.valor_a_ser_depositado_label.setFont(self.font)

        self.valor_a_ser_depositado_line = QtWidgets.QLineEdit(self.frame)
        self.valor_a_ser_depositado_line.setGeometry(QtCore.QRect(290, 70, 221, 20))

        self.confirmar_botao = QtWidgets.QPushButton("CONFIRMAR", self.frame)
        self.confirmar_botao.setGeometry(QtCore.QRect(110, 140, 211, 51))

        self.voltar_botao = QtWidgets.QPushButton("VOLTAR", self.frame)
        self.voltar_botao.setGeometry(QtCore.QRect(420, 140, 211, 51))

        self.font.setBold(True)
        self.font.setWeight(75)

        self.saldo_label = QtWidgets.QLabel("Saldo:", self)
        self.saldo_label.setGeometry(QtCore.QRect(580, 30, 191, 21))
        self.saldo_label.setFont(self.font)

        self.saldo_line = QtWidgets.QLineEdit(self)
        self.saldo_line.setGeometry(QtCore.QRect(630, 30, 141, 21))
        self.saldo_line.setEnabled(False)

    def set_style(self):
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0681818 rgba(14, 8, 73, 255), stop:0.607955 rgba(28, 17, 145, 255));")
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LEBANK_label.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.210227 rgba(255, 255, 0, 255), stop:0.778409 rgba(255, 255, 117, 255));")
        self.valor_a_ser_depositado_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.confirmar_botao.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.voltar_botao.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.saldo_label.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(19, 11, 98);")
        self.saldo_line.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(23, 14, 121);")


if __name__ == '__main__':
    root = QtWidgets.QApplication(sys.argv)
    app = Tela_Deposito()
    app.show()
    sys.exit(root.exec_())
