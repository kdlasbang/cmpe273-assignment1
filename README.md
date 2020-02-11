# cmpe273-assignment1
For tcp part A:
  I create a server can listen up to 5 connection(due to it is very few possible to congest for this assignment, it is not necessary to set up as 5.), for each connection from client will be connected via different thread. 
  At this time, server can connect with multiple clients. 



FOR UDP PART B:
  Comparing to the Requirement, I use a different method for lost detection and reliable message delivery. 
  The txt have 10000 lines, after reading the file, I set 1000 lines as a package. After each package sent, I will count the total len(line). If one line is lost, the total len(line) should be different between client and server. Then the client will send the same package again. 
  If the total lines of a file is 10050, then the left of 50 lines will count as a package as well.
  
  Example: in the package 1, it should have line 1-1000. If line 59 lost. The total len(line) of server should be total len(line1 to line1000) - len(line59). However, for the client, the total len(line) still len(line1 to line1000). At this time, client will send the same package to the server again. Until they have the same amount. 
