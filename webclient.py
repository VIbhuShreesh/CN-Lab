import socket
def download_web_page(hostname, port, path):
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((hostname, port))
    request = f"GET {path} HTTP/1.1\r\nHost:{hostname}\r\nConnection: close\r\n\r\n"
    client_socket.send(request.encode())
    response = b""
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        response += data
    client_socket.close()
    return response.decode()

hostname = ("www.example.com")
port = 80
path = "/"

response = download_web_page(hostname, port, path)

print(response)