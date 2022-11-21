import cv2
cap=cv2.VideoCapture(0) #0: kamera no
cap.set(3,640) #genişlik
cap.set(4,480) #yükseklik
cap.set(10,100)#parlaklık

while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
