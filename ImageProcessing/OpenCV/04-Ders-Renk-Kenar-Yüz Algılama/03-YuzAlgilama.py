import  cv2
import numpy as np

faceCascade=cv2.CascadeClassifier("../data/haarcascades/haarcascade_frontalface_default.xml")


def empty(a):
    pass

cv2.namedWindow("Ayar")
cv2.resizeWindow("Ayar", 640, 240)
cv2.createTrackbar("Skala", "Ayar", 5, 400, empty)
cv2.createTrackbar("Komsuluk", "Ayar", 3, 9, empty)

print("Yeni ayarları uygulamak için bir tuşa basın. Çıkmak için q'ya basın")

while True:
    img=cv2.imread("../data/res.jpg")
    img=img.copy()
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    skala = cv2.getTrackbarPos("Skala", "Ayar")
    komsuluk = cv2.getTrackbarPos("Komsuluk", "Ayar")
    faces=faceCascade.detectMultiScale(imgGray,(skala+101)/100,komsuluk+1)
#                                       scale factor, min neighbors


    
    #yüzleri çerçeveleme
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(w+w,y+h),(255,0,0),2)
        

    cv2.imshow("Sonuc",img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
        
    

cv2.destroyAllWindows()
