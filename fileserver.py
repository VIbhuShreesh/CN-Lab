import socket

def simple_file_server():
    s = socket.socket()
    s.bind(('localhost', 12345))
    s.listen(1)
    print("Waiting for file...")

    conn, addr = s.accept()
    print("Connected by", addr)

    filename = conn.recv(1024).decode()
    with open("received_" + filename, "wb") as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    print("File saved as received_" + filename)
    conn.close()

simple_file_server()
