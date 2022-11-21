import socket             
 
byte_message = bytes("cc", "utf-8")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     

ip="192.168.0.1"
port = 40000              
 
s.sendto(byte_message, (ip, port))

s.close()

