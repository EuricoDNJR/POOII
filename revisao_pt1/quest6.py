base = int(input("Insira a base: "))
expoente = int(input("Insira o expoente: "))
if expoente == 0:
    print("1")
else:
    while expoente != 1:
        base *= base
        expoente -= 1
    print(base)
