import socket
from queue import Queue
from threading import Thread 

class Listener():

    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__isActive = True

    def start(self):
        self.__sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sck.connect((self.__host, self.__port))
        self.__q = Queue()
        self.__collectorThread = Thread(target=self.__collectData, daemon=True)
        self.__collectorThread.start()
    
    def stop(self):
        self.__isActive = False

    def hasData(self):
        if self.__q.empty():
            return False
        else:
            return True
        
    def getData(self):
        data = self.__q.get(block=False)
        return data

# this runs as a thread
    def __collectData(self):
        data = b""
        while (self.__isActive):
            char = self.__sck.recv(1)
            if char == b"\n":
                self.__q.put(data.decode('utf-8').strip())
                data = b""
            else:
                data += char

        self.__sck.close()