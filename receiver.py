import socket
import subprocess



process = subprocess.Popen("python sender.py", shell=True)
pid = process.pid

#p = subprocess.Popen(["python", "sender.py"])

sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sck.bind(('', 49001))
sck.setblocking(30)

try:

    while True:

        try:
            data, address = sck.recvfrom(1024)
        except Exception as msg:
            print(msg)
            pass
        else:
            print("receiver: " + data.decode('utf-8'))

except KeyboardInterrupt:
    process.kill