from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Tela_Extrato(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Tela_Extrato, self).__init__(parent)
        self.settings()
        self.set_font()
        self.create_widgets()
        self.set_style()

    def settings(self):
        self.resize(800, 600)
        self.setWindowTitle("Extrato")

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
        self.frame.setGeometry(QtCore.QRect(0, 20, 811, 551))

        self.font.setPointSize(12)

        self.numero_label = QtWidgets.QLabel("Número:", self.frame)
        self.numero_label.setGeometry(QtCore.QRect(20, 0, 61, 31))
        self.numero_label.setFont(self.font)

        self.numero_line = QtWidgets.QLineEdit(self.frame)
        self.numero_line.setGeometry(QtCore.QRect(90, 10, 131, 20))
        self.numero_line.setEnabled(False)

        self.titular_label = QtWidgets.QLabel("Titular:", self.frame)
        self.titular_label.setGeometry(QtCore.QRect(260, 0, 51, 31))
        self.titular_label.setFont(self.font)

        self.titular_line = QtWidgets.QLineEdit(self.frame)
        self.titular_line.setGeometry(QtCore.QRect(320, 10, 391, 20))
        self.titular_line.setEnabled(False)

        self.saldo_label = QtWidgets.QLabel("Saldo:", self.frame)
        self.saldo_label.setGeometry(QtCore.QRect(30, 50, 51, 31))
        self.saldo_label.setFont(self.font)

        self.saldo_line = QtWidgets.QLineEdit(self.frame)
        self.saldo_line.setGeometry(QtCore.QRect(80, 60, 151, 20))
        self.saldo_line.setEnabled(False)

        self.voltar_botao = QtWidgets.QPushButton("Voltar", self.frame)
        self.voltar_botao.setGeometry(QtCore.QRect(310, 470, 211, 51))

        self.limite_label = QtWidgets.QLabel("Limite:", self.frame)
        self.limite_label.setGeometry(QtCore.QRect(260, 50, 51, 31))
        self.limite_label.setFont(self.font)

        self.limite_line = QtWidgets.QLineEdit(self.frame)
        self.limite_line.setGeometry(QtCore.QRect(320, 59, 391, 21))
        self.limite_line.setEnabled(False)

        self.historico_label = QtWidgets.QLabel("Histórico", self.frame)
        self.historico_label.setGeometry(QtCore.QRect(370, 80, 61, 31))
        self.historico_label.setFont(self.font)

        self.historico_line = QtWidgets.QTextEdit(self.frame)
        self.historico_line.setGeometry(QtCore.QRect(200, 110, 421, 361))
        self.historico_line.setEnabled(False)

    def set_style(self):
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LEBANK_label.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.210227 rgba(255, 255, 0, 255), stop:0.778409 rgba(255, 255, 117, 255));")
        self.numero_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titular_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.saldo_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.voltar_botao.setStyleSheet("background-color: rgb(255, 255, 0);")     
        self.limite_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.historico_label.setStyleSheet("background-color: rgb(255, 255, 255);")

if __name__ == '__main__':
    root = QtWidgets.QApplication(sys.argv)
    app = Tela_Extrato()
    app.show()
    sys.exit(root.exec_())
