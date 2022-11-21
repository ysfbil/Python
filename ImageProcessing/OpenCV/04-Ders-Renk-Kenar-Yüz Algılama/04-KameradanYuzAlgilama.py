import  cv2
import numpy as np

cap=cv2.VideoCapture(0) #0: kamera no
cap.set(3,640) #genişlik
cap.set(4,480) #yükseklik
cap.set(10,100)#parlaklık
faceCascade=cv2.CascadeClassifier("../data/haarcascades/haarcascade_frontalface_default.xml")

def empty(a):
    pass
 
cv2.namedWindow("Ayar")
cv2.resizeWindow("Ayar", 640, 240)
cv2.createTrackbar("Skala", "Ayar", 65, 400, empty)
cv2.createTrackbar("Komsuluk", "Ayar", 3, 9, empty)



while True:
    success,img=cap.read()
    img=img.copy()
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    skala = cv2.getTrackbarPos("Skala", "Ayar")
    komsuluk = cv2.getTrackbarPos("Komsuluk", "Ayar")

    faces=faceCascade.detectMultiScale(imgGray,(skala+101)/100,komsuluk+1)

    blank_image = np.zeros((100,640,3), np.uint8)
    cv2.putText(blank_image,"Skala:"+str((skala+101)/100)+" Komsuluk:"+str(komsuluk+1),(3,30),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    cv2.imshow("Ayar", blank_image)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(w+w,y+h),(255,0,0),2)

    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

