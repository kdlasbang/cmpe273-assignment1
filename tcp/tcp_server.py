import socket
import threading
import select

output = open("tcp_sever_out.txt", "w")
output.write("python3 tcp_server.py\n")

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(5)
    print("Server started at port"+str(TCP_PORT)+".")
    output.write("Server started at port"+str(TCP_PORT)+".\n")
    while True:
        r,w,x= select.select([s,],[],[],1)
        for i, s in enumerate(r):
            conn,addr=s.accept()
            t=threading.Thread(target=connect,args=(conn,addr))
            t.start()

def connect(conn, addr):
    cid=conn.recv(1024).decode()
    conn.send(("**GOT").encode())
    print("Connected Client:"+cid+".")
    output.write("Connected Client:"+cid+".\n")
    while True:
        data = conn.recv(1024)
        if not data:
            #print('No data received.')            
            break
        print(f"Received data:{cid}:{data.decode()}")
        output.write("Received data:"+cid+":"+data.decode()+"\n")
        conn.send("pong".encode())
    conn.close()
    
listen_forever()
output.close()
