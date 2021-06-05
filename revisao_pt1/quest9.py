tabuada_de = int(input("Montar a tabuada de: "))
comeca_de = int(input("Comecar por: "))
termina_em = int(input("Terminar em: "))

print("Vou montar a tabuada de %d comecando em %d e terminando em %d:" % (tabuada_de, comeca_de, termina_em))

for i in range(comeca_de, termina_em + 1):
    print("%d X %d = %d" % (tabuada_de, i, (tabuada_de * i)))

