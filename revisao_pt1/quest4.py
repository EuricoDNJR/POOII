l1 = float(input("Insira o tamanho do lado 1: "))
l2 = float(input("Insira o tamanho do lado 2: "))
l3 = float(input("Insira o tamanho do lado 3: "))

if (l1 + l2 > l3) or (l1 + l3 > l2) or (l2 + l3 > l1):
    if l1 == l2 == l3:
        print("Triangulo Equilatero")
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("Triangulo Isosceles")
    elif l1 != l2 != l3:
        print("Triangulo Escaleno")
else:
    print("Não forma um triangulo")


