import socket

def simple_file_client():
    s = socket.socket()
    s.connect(('localhost', 12345))

    filename = input("Enter filename to send: ")
    s.send(filename.encode())

    try:
        with open(filename, 'rb') as f:
            while (data := f.read(1024)):
                s.send(data)
        print("File sent successfully.")
    except FileNotFoundError:
        print("File not found.")

    s.close()

simple_file_client()
