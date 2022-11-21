# An example script to connect to Google using socket  
# programming in Python  
import socket # for socket  
import sys  
  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
print ("Socket successfully created") 
  
# default port for socket  
port = 80
  

host_ip = socket.gethostbyname('www.google.com')  

  
# connecting to the server  
s.connect((host_ip, port))

  
print ("the socket has successfully connected to google")  
