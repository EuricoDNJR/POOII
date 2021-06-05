n = int(input("Insira o numero: "))
if n == 0 or n == 1:
    print("1")
else:
    tot = 1
    while n != 1:
        tot *= n
        n -= 1
    print(tot)
