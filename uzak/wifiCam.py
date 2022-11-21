import cv2
import socket
import time


cap=cv2.VideoCapture("http://192.168.0.1:7060")


#capture = cv2.VideoCapture('rtsp://username:password@192.168.1.64/1')


#192.168.0.1:40000 UDP cc veri gönderiyoruz

byte_message = bytes("cc    ", "utf-8")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip="192.168.0.1"
port = 40000
s.sendto(byte_message, (ip, port))
s.close()


##8060 TCP
##GİDEN: lewei_cmd 4$?_
##GELEN: lewei_cmd

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8060
s.connect((ip, port))
byte_message = bytes("lewei_cmd                                   {oÊ_    ", "utf-8")
s.sendall(byte_message)
data = s.recv(1024)
s.close()
print ('Received', repr(data))

##7060 TCP
##GİDEN: lewei_cmd
##GELEN: lewei_cmd

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 7060
s.connect((ip, port))
byte_message = bytes("lewei_cmd                                    lewei_cmd                                    lewei_cmd                                    lewei_cmd                                    lewei_cmd                                    lewei_cmd                                    ","utf-8")


s.sendall(byte_message)
data = s.recv(1024)
s.close()
print ('Received', repr(data))


##s.close()  
##
#while True:
   #success,img=cap.read()
   #cv2.imshow("Video",img)
   
##   print (s.recv(2048))
##   time.sleep(0.4)
##   
##   if cv2.waitKey(1) & 0xFF == ord('q'):
##        break
