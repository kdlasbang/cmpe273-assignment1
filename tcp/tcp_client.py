import socket
import time,datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5003
BUFFER_SIZE = 1024


def send(id=0):
    #startTime = datetime.datetime(2020, 2, 9, 1, 57, 00)
    
    #while datetime.datetime.now() < startTime:
        #time.sleep(1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(f"{id}".encode())
    data = s.recv(BUFFER_SIZE)
    s.close()
    print("received data:", data.decode())


def get_client_id():
    id = input("Enter client id:")
    return id



send(get_client_id())
