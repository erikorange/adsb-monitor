import socket
from queue import Queue
from threading import Thread 

class Listener():

    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    def start(self):
        self.__sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sck.connect((self.__host, self.__port))
        self.__q = Queue()
        self.__collectorThread = Thread(target=self.__collectData, daemon=True)
        self.__collectorThread.start()
    
    def __collectData(self):
        data = b""
        while True:
            char = self.__sck.recv(1)
            if char == b"\n":
                self.__q.put(data.decode('utf-8').strip())
                data = b""
            else:
                data += char

    def getData(self):
        try:
            data = self.__q.get(block=False)
            return data
        
        except Queue.empty:
            raise BufferError("queue is empty")
