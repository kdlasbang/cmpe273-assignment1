import socket
import time

UDP_IP = '127.0.0.1'
UDP_PORT = 4001
BUFFER_SIZE = 1024

def write(result,m):
        with open('output.txt',m)as ff:
                for obj in result:
                        ff.write('%s\n' % obj)

#when client finish sending data, the server will save those data into txt.
#this is also helpful for me to check the complete data

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    package=[]    
    saver=[]      #saver save all the data then load into txt
    check=0       #check used to check the sum of sequence in a package,
                  #check whether the data have been lost in the transit process
    while True:
        # get the data sent to us
        data, ip = s.recvfrom(BUFFER_SIZE)
        
        if(data.decode()=="****DONE"):
            write(saver,'a')
            print("FINISH GETTING ",len(saver)," DATA FROM {}".format(ip))
            saver=[]
            continue

        if(data.decode()=="***CHECK"):
            # reply check num to the client
            cc=str(check)
            s.sendto(cc.encode(), ip)
            continue

        if(data.decode()=="***RESEND!"):
            # got the message from client that last package need to be resent
            print("Data Lost or been Modified,Begin Receiving Last Package.")
            package=[]
            check=0
            continue

        if(data.decode()=="***SUCCESS!"):
            #after checking up, last package is completed, turn data to saver[]
            print("SUCCESSFULLY GOT ",len(package)," LINES FROM--",ip)
            saver+=package
            package=[]
            check=0
            continue
        
        words=data.decode().split(':')
        package.append(words[1])
        check+=int(words[0])

        
listen_forever()
