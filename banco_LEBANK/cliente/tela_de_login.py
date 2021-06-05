from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Tela_Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Tela_Login, self).__init__(parent)
        self.settings()
        self.set_font()
        self.create_widgets()
        self.set_style()

    def settings(self):
        self.resize(800, 600)
        self.setWindowTitle("Login")

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
        self.frame.setGeometry(QtCore.QRect(0, 150, 811, 211))

        self.font.setPointSize(12)

        self.numero_da_conta_label = QtWidgets.QLabel("Número da conta:", self.frame)
        self.numero_da_conta_label.setGeometry(QtCore.QRect(70, 20, 131, 31))
        self.numero_da_conta_label.setFont(self.font)

        self.numero_da_conta_line = QtWidgets.QLineEdit(self.frame)
        self.numero_da_conta_line.setGeometry(QtCore.QRect(240, 30, 391, 20))

        self.senha_label = QtWidgets.QLabel("Senha:", self.frame)
        self.senha_label.setGeometry(QtCore.QRect(150, 80, 91, 31))
        self.senha_label.setFont(self.font)

        self.senha_line = QtWidgets.QLineEdit(self.frame)
        self.senha_line.setGeometry(QtCore.QRect(240, 90, 391, 20))

        self.logar_botao = QtWidgets.QPushButton("Logar", self.frame)
        self.logar_botao.setGeometry(QtCore.QRect(120, 140, 211, 51))

        self.voltar_botao = QtWidgets.QPushButton("Voltar", self.frame)
        self.voltar_botao.setGeometry(QtCore.QRect(510, 140, 211, 51))

    def set_style(self):
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0681818 rgba(14, 8, 73, 255), stop:0.607955 rgba(28, 17, 145, 255));")
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LEBANK_label.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.210227 rgba(255, 255, 0, 255), stop:0.778409 rgba(255, 255, 117, 255));")
        self.numero_da_conta_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.senha_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.logar_botao.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.voltar_botao.setStyleSheet("background-color: rgb(255, 255, 0);")


if __name__ == '__main__':
    root = QtWidgets.QApplication(sys.argv)
    app = Tela_Login()
    app.show()
    sys.exit(root.exec_())
