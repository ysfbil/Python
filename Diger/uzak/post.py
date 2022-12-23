import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddr = socket.gethostbyname( 'ibrahimbilgen.com' )
s.connect(( ipaddr,80 ))

data = "name=Yusuf&age=42\n\n"

header = ( """
POST /test_post.php HTTP/1.1
Host: ibrahimbilgen.com
Content-Type: application/x-www-form-urlencoded
""" )

#Accept-Encoding: gzip, deflate şeklinde bir satırı headera eklediğimizde veri sıkıştırılmış olarak geldiğinden anlamsız karakterler içerir.

contentLength = "Content-Length: " + str( len( data ) ) + "\n\n"
request =bytes( header + contentLength + data,"utf-8")
s.sendall( request )
response = s.recv( 4096 )
s.close()
print (request)
print("-------------------------------")
print (repr(response))
sys.exit( 0 )
