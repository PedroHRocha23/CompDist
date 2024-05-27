#Pedro Rocha  10396190
#Camila Faleiros 10395818
#Gabriel Gadelha 10395945
#Fernanda Aiko 10395952

### Cliente de Chat

import socket
import threading

# Configurações do cliente
HOST = '127.0.0.1'  # IP do servidor
PORT = 5000         # Porta de conexão

# Conectando ao servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Função para receber mensagens do servidor
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Erro ao receber dados do servidor.")
            client.close()
            break

# Função para enviar mensagens ao servidor
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

# Solicita o nickname do usuário
nickname = input("Escolha seu nickname: ")

# Inicia threads para escuta e envio de mensagens
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


