'Chat Room Connection - Client-To-Client'
import threading
import socket
host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []


def broadcast(message):
    for client in clients:
        client.send(message)

# Funcion de las conexiones


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{nombre} ha abandonado!'.encode('utf-8'))
            aliases.remove(alias)
            break
# Conexion del cliente


def receive():
    while True:
        print('Server corriendo ...')
        client, address = server.accept()
        print(f'Conexion establecida {str(address)}')
        client.send('nombre?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'El nombre es {nombre}'.encode('utf-8'))
        broadcast(f'{nombre} se ha conectado'.encode('utf-8'))
        client.send('Conectado!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()
