import socket
import time

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
# got data from the upload.txt

    ack=0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    i=0
    ii=0
    
    while(i<len(upload)):
        #print("1")
        ack+=len(upload[i])
        #Before I send the data, I will add up the len of this line.
        #If this line data get lost in the transit process, the server
        #should have one len(line) less. For example, one len(line of data)
        # is 1, I have sent 100 lines. The 7th line is lost. For client,
        #total nums of len(line) should be 100, while for server should be 99.
        #Then I will resend this package again. 

        s.sendto(upload[i].encode(), (UDP_IP, UDP_PORT))
        i+=1
        
        if(i%1000==0 or i==len(upload)):
            try:
                s.settimeout(3)
                s.sendto("***CHECK".encode(), (UDP_IP, UDP_PORT))
                data, ip = s.recvfrom(BUFFER_SIZE)
                s.settimeout(None)
            except socket.timeout:
                print("timeout")
                s.sendto("***CHECK".encode(), (UDP_IP, UDP_PORT))
                data, ip = s.recvfrom(BUFFER_SIZE)
                s.settimeout(None)
            if(data.decode()==str(ack)):
                print("SUCCESSFULLY SEND ",i," LINES TO SERVER.")
                s.sendto("SUCCESS!".encode(), (UDP_IP, UDP_PORT))
                ack=0
                ii=i
                continue
            else:
                print("PACKAGE LOSE DETECT, RESEND LAST PKG.")
                s.sendto("***RESEND!".encode(), (UDP_IP, UDP_PORT))
                i=ii
                ack=0
                continue

        #I set 1000 lines as a package, for each package need to be check
        #When the several lines less than 1000, those serveral lines can be
        #considered as a package and need to be checked

        
    s.sendto("****DONE".encode(), (UDP_IP, UDP_PORT))
    print("FINISH SENDING DATA TO--{}: {} LINES.".format(UDP_IP, i))
    print("CLOSED CONNECTION")

        
    #except socket.error:
        #print("Error! {}".format(socket.error))
        #exit()



send()
