import socket
import time

output = open("udp_sever_out.txt", "w")
output.write("python3 udp_server.py\n\n")

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024

def write(result,m):
        with open('data.txt',m)as ff:
                for obj in result:
                        ff.write('%s\n' % obj)

#when client finish sending data, the server will save those data into txt.
#this is also helpful for me to check the complete data

def listen_forever():
    observer=0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    package=[]    
    saver=[]      #saver save all the data then load into txt
    check=0       #check used to check the sum of sequence in a package,
                  #check whether the data have been lost in the transit process
    print("Server started at port",UDP_PORT,".")
    output.write("Server started at port"+str(UDP_PORT)+".\n")
    
    while True:
        # get the data sent to us
        data, ip = s.recvfrom(BUFFER_SIZE)
        if(observer==0):
            print("Accepting a file upload...")
            output.write("Accepting a file upload...\n")
            observer=observer+1
        
        
        if(data.decode()=="****DONE"):
            write(saver,'a')
            print("Upload successfully completed.")
            output.write("Upload successfully completed.\n")
            saver=[]
            observer=0
            continue

        if(data.decode()=="***CHECK"):
            # reply check num to the client
            cc=str(check)
            s.sendto(cc.encode(), ip)
            continue

        if(data.decode()=="***RESEND!"):
            # got the message from client that last package need to be resent
            package=[]
            check=0
            continue

        if(data.decode()=="***SUCCESS!"):
            #after checking up, last package is completed, turn data to saver[]
            saver+=package
            package=[]
            check=0
            continue
        
        words=data.decode().split(':')
        package.append(words[1])
        check+=int(words[0])

        
listen_forever()
output.close()
