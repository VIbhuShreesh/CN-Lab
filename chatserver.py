import socket
import threading

clients = []


def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break  # Client has disconnected
            print(f"Received from {client_address}: {message}")
            for client in clients:
                if client != client_socket:
                    client.sendall(message.encode())
        except:
            break
    clients.remove(client_socket)
    client_socket.close()


def chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 55555))
    server_socket.listen(5)
    print("Server listening on port 55555...")
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()


if __name__ == '__main__':
    chat_server()
