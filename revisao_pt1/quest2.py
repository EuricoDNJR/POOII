peso = float(input("Insira o peso dos peixes: "))
qt_ultrapassada = peso - 50
if qt_ultrapassada < 0:
    qt_ultrapassada = 0
multa = qt_ultrapassada * 4
print("Quantidade de quilos alem do limite: %.1f" % qt_ultrapassada)
print("Multa: %.2f" % multa)
