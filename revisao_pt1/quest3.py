ganho_por_hora = float(input("Insira o valor que ganha por hora: "))
numero_de_horas = float(input("Insira o numero de horas trabalhadas no mes: "))
salario_bruto = ganho_por_hora * numero_de_horas
print("Salario bruto: %.2f" % salario_bruto)
IR = salario_bruto * 0.11
print("IR: %.2f" % IR)
INSS = salario_bruto * 0.08
print("INSS: %.2f" % INSS)
sindicato = salario_bruto * 0.05
print("Sindicato: %.2f" % sindicato)
print("Salario liquido: %.2f" % (salario_bruto - IR - INSS - sindicato))
