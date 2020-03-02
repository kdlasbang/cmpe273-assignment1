import socket
import time,datetime
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
cid= sys.argv[1]
delay=  int(sys.argv[2])
num= int(sys.argv[3])
output= open('tcp_client_out.txt','a')
output.write("python3 "+sys.argv[0]+" "+sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+"\n")

def send(num):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(cid.encode())
    ack=s.recv(BUFFER_SIZE).decode()
    if(ack!="**GOT"):
        print("error")
    while(num>0):
        ping="ping"
        s.send(ping.encode())
        print("Sending data:ping")
        output.write("Sending data:ping\n")
        data = s.recv(BUFFER_SIZE)
        print("Received data:", data.decode())
        output.write("Received data:"+data.decode()+"\n")
        num=num-1
        if(num==0):
            break
        time.sleep(delay)
    s.close()

send(num)
output.close()
