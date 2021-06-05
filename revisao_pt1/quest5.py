qts_litros = float(input("Insira quantos litros foram vendidos: "))
tipo_combustivel = input("Insira o tipo de combustivel( A - alcool, G - gasolina): ")
if tipo_combustivel == "A":
    if qts_litros <= 20:
        valor_bruto = qts_litros * 3.45
        desconto = qts_litros * 0.03
        print("Valor a ser pago: %.2f" % (valor_bruto - desconto))
    else:
        valor_bruto = qts_litros * 3.45
        desconto = qts_litros * 0.05
        print("Valor a ser pago: %.2f" % (valor_bruto - desconto))
elif tipo_combustivel == "G":
    if qts_litros <= 20:
        valor_bruto = qts_litros * 4.53
        desconto = qts_litros * 0.04
        print("Valor a ser pago: %.2f" % (valor_bruto - desconto))
    else:
        valor_bruto = qts_litros * 4.53
        desconto = qts_litros * 0.06
        print("Valor a ser pago: %.2f" % (valor_bruto - desconto))