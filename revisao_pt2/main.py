from conta import Conta, Cliente

'''c1 = Conta('123-4', 'Joao', 120.0)
c2 = Conta('567-8', 'Jose', 0)

transferiu = c2.transfere(c1, 10.0)
if not transferiu:
    print("Não transferiu")
else:
    print("Transferiu")

transferiu = c1.transfere(c2, 10.0)
if not transferiu:
    print("Não transferiu")
else:
    print("Transferiu")

print(c1.saldo)
print(c2.saldo)
'''

cliente1 = Cliente('Joao', 'Oliveira', '123456789-01')
cliente2 = Cliente('Jose', 'Azevedo', '222222222-22')
conta1 = Conta('123-4', cliente1, 1000.0)
conta2 = Conta('123-5', cliente2, 1000.0)
conta1.deposita(100.0)
conta1.saca(50.0)
conta1.transfere_para(conta2, 200.0)
conta1.extrato()
conta1.historico.imprime()
conta2.historico.imprime()
print(Conta.get_total_contas())



