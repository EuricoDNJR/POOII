import socket
ip = "localhost"
port = 8000
addr = (ip, port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
while 1:
    mensagem = input("digite uma mensagem para enviar ao servidor: ")
    client_socket.send(mensagem.encode())
    if mensagem == "flw":
        client_socket.close()
        print("Conexão fechada pelo Cliente...")
        break
    mensagem_recebida = client_socket.recv(1024).decode()
    print("mensagem recebida: " + mensagem_recebida)
    if mensagem_recebida == "flw":
        client_socket.close()
        print("Conexão fechada pelo Servidor...")
        break
