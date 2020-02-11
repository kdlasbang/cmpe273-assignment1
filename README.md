# cmpe273-assignment1
For tcp part A:
  I create a server can listen up to 5 connection(due to it is very few possible to congest for this assignment, it is not necessary to set up as 5.), for each connection from client will be connected via different thread. 
  At this time, server can connect with multiple clients. 



FOR UDP PART B:
  I set 1000(default, but I can change) lines as a package. After each package sent, I will count the sum of sequence ID in a package. If one line is lost, the sum of sequence ID should be different between client and server. If the client detect that the sum of sequence ID are different, the client will send the same package again until they got the same number.  

  Example: in the package 1, it should have line 1-1000. If line 59 lost. The total sum of sequence ID should be 500500-59. However, for the client, the total sum of sequence ID should stay the same,500500. At this time, client will send the same package1 to the server again. Until they have the same amount. 

  I set up timeout alert that, if client still not received response from server, after setting seconds, the client will resend the message to server and wait for the response. (client will keep sending per several seconds until it get the response from server)
  
  Moreover, due to the sum of sequence ID for each package is different. I don't need to set up package ID. If any error happen, the client will send the same package, and the server will keep previous package and wait to receive the resend package again.
