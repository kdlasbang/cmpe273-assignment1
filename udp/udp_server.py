import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 4001
BUFFER_SIZE = 1024
MESSAGE = "get 1000 lines, checking ack"

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    package=[]
    saver=[]
    check=0
    i=0
    while True:
        # get the data sent to us
        data, ip = s.recvfrom(BUFFER_SIZE)
        package.append(data.decode(encoding="utf-8"))
        check+=len(package[i])
        i+=1
        if(len(package)==1000):
            print("{}: {}".format(ip, MESSAGE))
            # reply back to the client
            cc=str(check)
            s.sendto(cc.encode(), ip)
            data, ip = s.recvfrom(BUFFER_SIZE)
            if(data.decode(encoding="utf-8")=="RESEND!"):
                package=[]
                check=0
                i=0
                continue
            else:
                saver+=package
                package=[]
                check=0
                i=0
                if(len(saver)%10000==0):
                    
                    print("finish accept 10000 lines from {}".format(ip))
                continue
        
listen_forever()
