# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_de_cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Tela_Cadastro(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Tela_Cadastro, self).__init__(parent)
        self.settings()
        self.set_font()
        self.create_widgets()
        self.set_style()

    def settings(self):
        self.resize(800, 600)
        self.setWindowTitle("Cadastro")

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
        self.frame.setGeometry(QtCore.QRect(0, 90, 811, 381))

        self.font.setPointSize(12)

        self.nome_label = QtWidgets.QLabel("Nome:", self.frame)
        self.nome_label.setGeometry(QtCore.QRect(130, 60, 51, 31))
        self.nome_label.setFont(self.font)

        self.nome_line = QtWidgets.QLineEdit(self.frame)
        self.nome_line.setGeometry(QtCore.QRect(210, 70, 391, 20))

        self.sobrenome_label = QtWidgets.QLabel("Sobrenome:", self.frame)
        self.sobrenome_label.setGeometry(QtCore.QRect(90, 110, 91, 31))
        self.sobrenome_label.setFont(self.font)

        self.sobrenome_line = QtWidgets.QLineEdit(self.frame)
        self.sobrenome_line.setGeometry(QtCore.QRect(210, 120, 391, 20))

        self.cpf_label = QtWidgets.QLabel("CPF:", self.frame)
        self.cpf_label.setGeometry(QtCore.QRect(140, 160, 41, 31))
        self.cpf_label.setFont(self.font)
        
        self.cpf_line = QtWidgets.QLineEdit(self.frame)
        self.cpf_line.setGeometry(QtCore.QRect(210, 170, 391, 20))

        self.confirmar_botao = QtWidgets.QPushButton("CONFIRMAR", self.frame)
        self.confirmar_botao.setGeometry(QtCore.QRect(150, 280, 211, 51))
        
        self.senha_label = QtWidgets.QLabel("Senha:", self.frame)
        self.senha_label.setGeometry(QtCore.QRect(130, 210, 51, 31))
        self.senha_label.setFont(self.font)

        self.senha_line = QtWidgets.QLineEdit(self.frame)
        self.senha_line.setGeometry(QtCore.QRect(210, 220, 391, 20))
 
        self.voltar_botao = QtWidgets.QPushButton("VOLTAR", self.frame)
        self.voltar_botao.setGeometry(QtCore.QRect(460, 280, 211, 51))

    def set_style(self):
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0681818 rgba(14, 8, 73, 255), stop:0.607955 rgba(28, 17, 145, 255));")
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LEBANK_label.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(28, 17, 145); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.210227 rgba(255, 255, 0, 255), stop:0.778409 rgba(255, 255, 117, 255));")
        self.nome_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sobrenome_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cpf_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.confirmar_botao.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.senha_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.voltar_botao.setStyleSheet("background-color: rgb(255, 255, 0);")

if __name__ == '__main__':
    root = QtWidgets.QApplication(sys.argv)
    app = Tela_Cadastro()
    app.show()
    sys.exit(root.exec_())
