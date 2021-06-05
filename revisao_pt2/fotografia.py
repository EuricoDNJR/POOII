from skimage.io import imread
import matplotlib.pyplot as plt
import datetime

class Pessoa:
    __slots__ = ['_nome', '_cpf', '_endereco', '_telefone']

    def __init__(self, nome, cpf, endereco, telefone):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    def exibir(self):
        print('Nome: ' + self._nome)
        print('CPF : ' + self._cpf)
        print('Endereco: ' + self._endereco)
        print('Telefone: ' + self._telefone)


class Fotografia:
    _quantidade_fotos = 0
    __slots__ = ['_foto', '_fotografo', '_data', '_proprietario']

    def __init__(self, foto, fotografo, proprietario):
        self._foto = imread(foto)
        self._fotografo = fotografo
        self._data = datetime.datetime.today()
        self._proprietario = proprietario
        Fotografia._quantidade_fotos += 1

    @staticmethod
    def get_total_fotos():
        return Fotografia._quantidade_fotos

    @property
    def foto(self):
        return self._foto

    @foto.setter
    def foto(self, foto):
        self._foto = foto

    @property
    def fotografo(self):
        return self._fotografo

    @fotografo.setter
    def fotografo(self, fotografo):
        self._fotografo = fotografo

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def proprietario(self):
        return self._proprietario

    @proprietario.setter
    def proprietario(self, proprietario):
        self._proprietario = proprietario

    def propriedades_fotografia(self):
        plt.imshow(self._foto)
        plt.show()
        print("Dimensão da foto:")
        print(self._foto.shape)
        print("FOTOGRAFO:")
        print(self._fotografo.exibir())
        print("Data/hora: " + str(self._data))
