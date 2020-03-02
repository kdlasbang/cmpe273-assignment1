import socket
import time
import math

output = open("udp_client_out.txt", "w")
output.write("python3 udp_client.py\n\n")

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
upload=[]
pkg_size=1000
index=[]

def settimeout(s,UDP_IP,UDP_PORT):
    try:
        #--------set timeout function outside, recursion-----
        # get back the original try here
        s.settimeout(3)
        s.sendto("***CHECK".encode(), (UDP_IP, UDP_PORT))
        data, ip = s.recvfrom(BUFFER_SIZE)
        s.settimeout(None)
        return data.decode()
    except socket.timeout:
        #print("timeout,re-ask for the ack")
        settimeout(s,UDP_IP,UDP_PORT)



def send():
    
    with open("upload.txt","r") as f:
        db=f.read().splitlines()

    for line in db:
        words=line.split(':')
        upload.append(words[1])
        index.append(int(words[0]))
    
# got data from the upload.txt
    try:
        ack=0
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Connected to the server.")
        output.write("Connected to the server.\n")
        print("Starting a file (upload.txt) upload...")
        output.write("Starting a file (upload.txt) upload...\n")
        i=0
        ii=0

        while(i<len(upload)):
            ack+=index[i]
            #Before I send the data, I will add up the sequence ID of a package.
            #If one data get lost in the transit process, the sum of sequence ID
            #between server and client should be different.
            #For example, for package1, sum of sequence ID is 500500. 
            # if sequence 499 get lost, the sequence ID from server will be
            #500401. Futhermore,I don't need to set up package ID, because
            #the sum of sequence in each package is unique. 


            s.sendto(db[i].encode(), (UDP_IP, UDP_PORT))
            i+=1
            
            if(i%pkg_size==0 or i==len(upload)):
                scheck=settimeout(s,UDP_IP,UDP_PORT)
                
                if(scheck==str(ack)):
                    strack="Received ack("+str(math.ceil(i/pkg_size))+") from the server."
                    print(strack)
                    output.write(strack+"\n")
                    s.sendto("***SUCCESS!".encode(), (UDP_IP, UDP_PORT))
                    ack=0
                    ii=i
                    continue
                else:
                    #print("PACKAGE LOSE DETECT, RESEND LAST PKG.")
                    s.sendto("***RESEND!".encode(), (UDP_IP, UDP_PORT))
                    i=ii
                    ack=0
                    continue

            #I set 1000 lines as a package.
            #When the last several lines less than 1000,
            #those serveral lines can be considered as a package.

            
        s.sendto("****DONE".encode(), (UDP_IP, UDP_PORT))
        print("File upload successfully completed.")
        output.write("File upload successfully completed.\n")

        
    except socket.error:
        print("Error! {}".format(socket.error))
        output.write("Error! {}".format(socket.error))
        exit()



send()
output.close()
