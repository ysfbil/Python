import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50000))
msg=bytes("Hello, world","UTF-8")
s.sendall(msg)
data = s.recv(1024)
s.close()
print ('Received', repr(data))
input();
