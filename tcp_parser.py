import socket
import signal

def handler(signum, frame):
    print('Ctrl+C was pressed. Exiting gracefully.')
    print(str(idx))
    exit(0)

def readline(sock):
    data = b""
    while True:
        char = sock.recv(1)
        if not char:
            return data  # Connection closed
        data += char
        if char == b"\n":
            return data.decode().strip()

signal.signal(signal.SIGINT, handler)
idx = 0

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 30003))

while True:
    s = readline(client_socket)
    print(s)
    idx+=1
