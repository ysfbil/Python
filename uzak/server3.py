import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50000))
s.listen(1)
conn, addr = s.accept()  #bu döngü içerisinde olmadığından tekbir bağlantı kabul eder

page="""<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>"""

page_byte=bytes(page,"UTF-8")

while 1:
    data = conn.recv(1024)
    if not data: #veri akışı tamamlandığında iletişimi kesiyoruz.
        break
    conn.sendall(page_byte) #gelen veriyi geri gönderiyoruz.
    print(page_byte)
    print("-------------------------")
    print(data)
conn.close()
