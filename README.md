# cmpe273-assignment1
For tcp part A:
  I create a server can listen up to 5 connection(due to it is very few possible to congest for this assignment, it is not necessary to set up as 5.), for each connection from client will be connected via different thread. 
  At this time, server can connect with multiple clients. 



FOR UDP PART B:
  I set 1000(default, but I can change) lines as a package. After each package sent, I will count the total len(line). If one line is lost, the total len(line) should be different between client and server. If the client detect that the total nums of len(line) are different, the client will send the same package again until they got the same number.  

  Example: in the package 1, it should have line 1-1000. If line 59 lost. The total len(line) of server should be total len(line1 to line1000) - len(line59). However, for the client, the total len(line) still len(line1 to line1000). At this time, client will send the same package1 to the server again. Until they have the same amount. 

  I set up timeout alert that, if client still not received response from server, after setting seconds, the client will resend the message to server and wait for the response. (client will keep sending per several seconds until it get the response from server)
  
