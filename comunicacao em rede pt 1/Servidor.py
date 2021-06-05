import socket
host = '0.0.0.0'
port = 8000
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)
print("aguardando conexao...")
con, cliente = serv_socket.accept()

print("conectado")
print("aguardando mensagem...")

while 1:
    recebe = con.recv(1024)
    mensagem_recebida = recebe.decode()
    print("mensagem recebida: " + mensagem_recebida)
    if mensagem_recebida == "flw":
        serv_socket.close()
        print("Conexão fechada pelo Cliente...")
        break
    enviar = input("digite uma mensagem para enviar ao cliente: ")
    con.send(enviar.encode())
    if enviar == "flw":
        serv_socket.close()
        print("Conexão fechada pelo Servidor...")
        break
