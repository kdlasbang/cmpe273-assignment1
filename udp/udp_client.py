import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 4001
BUFFER_SIZE = 1024
upload=[]

def send():
    
    with open("upload.txt","r") as f:
        data=f.read().splitlines()

    for line in data:
        words=line.split(':')
        upload.append(words[1])
    try:
        ack=0
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        i=0
        while(i<10000):
            ack+=len(upload[i])
            s.sendto(upload[i].encode(), (UDP_IP, UDP_PORT))
            i+=1
            if(i%1000==0):
                data, ip = s.recvfrom(BUFFER_SIZE)
                if(data.decode()==str(ack)):
                    print("successfully already send ",i," lines")
                    s.sendto("SUCCESS!".encode(), (UDP_IP, UDP_PORT))
                    ack=0
                    continue
                else:
                    s.sendto("RESEND!".encode(), (UDP_IP, UDP_PORT))
                    i=i-(i%1000)
                    ack=0
                    continue
        print("successfully sent to: {}: {} lines".format(ip, i))
        
    except socket.error:
        print("Error! {}".format(socket.error))
        exit()


send()


#send(get_client_id())
