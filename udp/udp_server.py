import socket
import time

UDP_IP = '127.0.0.1'
UDP_PORT = 4001
BUFFER_SIZE = 1024
MESSAGE = "get 1000 lines, checking ack"

def write(result,m):
        with open('output.txt',m)as ff:
                for obj in result:
                        ff.write('%s\n' % obj)

#when client finish sending data, the server will save those data into txt.
#this is also helpful for me to check the complete data

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    package=[]    #I set that one package can load 1000 lines
    saver=[]      #saver save all the data then load into txt
    check=0       #check used to check the len of each line, check whether
                  #the data have been modifed in the transit process
    i=0           #index of line
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
            i=0
            continue

        if(data.decode()=="SUCCESS!"):
            #after checking up, last package is completed, turn data to saver[]
            print("SUCCESSFULLY GOT 1000 LINES FROM--",ip)
            saver+=package[:1000]
            package=[]
            check=0
            i=0
            continue
        
        package.append(data.decode(encoding="utf-8"))
        check+=len(package[i])
        i+=1

        
listen_forever()
