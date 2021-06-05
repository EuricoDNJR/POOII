from fotografia import Fotografia, Pessoa

fotografo1 = Pessoa('Joao', '123456789 - 01', 'Rua liberdade', '99977885522')
proprietario1 = Pessoa('Tiago', '123456111 - 01', 'Rua flor', '2222285522')
foto1 = Fotografia('gtr.jpg', fotografo1, proprietario1)
foto1.propriedades_fotografia()
print('Total de fotos: ' + str(Fotografia.get_total_fotos()))

fotografo2 = Pessoa('Barone', '221456789 - 01', 'Rua Natal', '55577885522')
proprietario2 = Pessoa('Camila', '773456111 - 01', 'Rua Trave', '4002285522')
foto2 = Fotografia('skyline.jpg', fotografo2, proprietario2)
foto2.propriedades_fotografia()
print('Total de fotos: ' + str(Fotografia.get_total_fotos()))
