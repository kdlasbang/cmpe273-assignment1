import socket
import threading
import select

TCP_IP = '127.0.0.1'
TCP_PORT = 5003
BUFFER_SIZE = 1024

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(5)
    print("Now,accepting connection:")
    while True:
        r,w,x= select.select([s,],[],[],1)
        for i, s in enumerate(r):
            conn,addr=s.accept()
            t=threading.Thread(target=connect,args=(conn,addr))
            t.start()

def connect(conn, addr):
    print(f'Connection address:{addr}')
    while True:
        data = conn.recv(1024)
        if not data:
            #print('No data received.')            
            break
        print(f"received-----Client id: {data.decode()}")
        conn.send("pong".encode())
    conn.close()
    
listen_forever()
