qts_vezes = int(input("Quantas vezes deseja calcular?: "))
while qts_vezes > 0:
    n = int(input("Insira o numero: "))
    if (n >= 0) and (n < 16):
        if n == 0 or n == 1:
            print("1")
        else:
            tot = 1
            while n != 1:
                tot *= n
                n -= 1
            print(tot)
        qts_vezes -= 1
    else:
        print("Quebrou a regra!")