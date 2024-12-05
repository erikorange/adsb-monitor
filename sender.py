import socket
import datetime
import time

sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sck.connect(('127.0.0.1', 49001))

while True:
    dt = str(datetime.datetime.now())
    msg = bytes(dt, 'utf-8')
    retry = True
    while (retry):
        try:
            sck.send(msg)
        except ConnectionRefusedError:
            time.sleep(1)
        except:
            time.sleep(1)
        else:
            print("sender: " + dt)
            retry = False

    time.sleep(1)
