from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Tela_Inicial(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Tela_Inicial, self).__init__(parent)
        self.settings()
        self.set_font()
        self.create_widgets()
        self.set_style()

    def settings(self):
        self.resize(800, 463)
        self.setWindowTitle("Inicio")
        

    def set_font(self):
        self.font = QtGui.QFont()
        self.font.setFamily("Impact")
        self.font.setPointSize(12)
        self.font.setBold(False)
        self.font.setWeight(50)

    def create_widgets(self):
        self.cadastrar_se_botao = QtWidgets.QPushButton("CADASTRE-SE", self)
        self.cadastrar_se_botao.setGeometry(QtCore.QRect(160, 170, 171, 121))  
        self.cadastrar_se_botao.setFont(self.font)  
    
        self.login_botao = QtWidgets.QPushButton("LOGIN", self)
        self.login_botao.setGeometry(QtCore.QRect(460, 170, 171, 121))
        self.login_botao.setFont(self.font)
            
        self.LEBANK_label = QtWidgets.QLabel("LEBANK", self)
        self.LEBANK_label.setGeometry(QtCore.QRect(0, 0, 811, 20))
        self.LEBANK_label.setAlignment(QtCore.Qt.AlignCenter)
        self.font.setFamily("Arial")
        self.font.setPointSize(16)
        self.LEBANK_label.setFont(self.font)
        
    def set_style(self):
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0681818 rgba(14, 8, 73, 255), stop:0.607955 rgba(28, 17, 145, 255));")
        self.cadastrar_se_botao.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145);")
        self.login_botao.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145);")
        self.LEBANK_label.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.210227 rgba(255, 255, 0, 255), stop:0.778409 rgba(255, 255, 117, 255));")


if __name__ == '__main__':
    root = QtWidgets.QApplication(sys.argv)
    app = Tela_Inicial()
    app.show()
    sys.exit(root.exec_())