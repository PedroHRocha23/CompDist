#Pedro Rocha  10396190
#Camila Faleiros 10395818
#Gabriel Gadelha 10395945
#Fernanda Aiko 10395952

### Servidor de Chat

import socket
import threading

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 5000         # Porta de escuta

# Lista de clientes conectados
clients = []
nicknames = []

# Função para transmitir mensagens para todos os clientes conectados
def broadcast(message):
    for client in clients:
        client.send(message)

# Função para tratar a conexão de um cliente
def handle_client(client):
    while True:
        try:
            # Recebe e transmite mensagens
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f'{nickname} saiu do chat!'.encode('utf-8'))
            break

# Função principal para receber conexões
def receive():
    server.listen()
    print('Servidor esperando por conexões...')
    while True:
        client, address = server.accept()
        print(f'Conectado com {str(address)}')

        # Solicita e armazena o nickname do cliente
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname do cliente é {nickname}')
        broadcast(f'{nickname} entrou no chat!'.encode('utf-8'))
        client.send('Conectado ao servidor!'.encode('utf-8'))

        # Inicia uma thread para tratar o cliente
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Inicia o servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

receive()

