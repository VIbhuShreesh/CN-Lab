import socket
import threading
def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        print(message)

def chat_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 55555))
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    while True:
        message = input()
        client_socket.sendall(message.encode())

if __name__ == '__main__':
    chat_client()
