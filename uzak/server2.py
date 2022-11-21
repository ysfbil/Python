import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50000))
s.listen(1)
conn, addr = s.accept()  #bu döngü içerisinde olmadığından tekbir bağlantı kabul eder
while 1:
    data = conn.recv(1024)
    if not data: #veri akışı tamamlandığında iletişimi kesiyoruz.
        break
    conn.sendall(data) #gelen veriyi geri gönderiyoruz.
    print(data)
conn.close()
