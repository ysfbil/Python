import cv2
from datetime import datetime


#plakaCascade=cv2.CascadeClassifier("../data/haarcascades/haarcascade_russian_plate_number.xml") #rus plaka
plakaCascade=cv2.CascadeClassifier("../data/turkish-license-plate-detector-master/data/cascade.xml") #turk plaka

minArea=500
color=(255,0,255)
count=0


cap=cv2.VideoCapture(0) #0: kamera no
cap.set(3,640) #genişlik
cap.set(4,480) #yükseklik
cap.set(10,100)#parlaklık

def empty(a):
    pass
 
cv2.namedWindow("Ayar")
cv2.resizeWindow("Ayar", 640, 240)
cv2.createTrackbar("ScaleFactor", "Ayar", 31, 100, empty)
cv2.createTrackbar("MinNeighbors", "Ayar", 52, 100, empty)

while True:

    now = datetime.now()

    current_time = now.strftime("%H_%M_%S_")
    
    #success,img=cap.read()
    img=cv2.imread("../data/trcar2.jpg")

    sf = cv2.getTrackbarPos("ScaleFactor", "Ayar")/10+1.1
    mn = cv2.getTrackbarPos("MinNeighbors", "Ayar")+1
    
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    plakalar=plakaCascade.detectMultiScale(imgGray,sf,mn)

    for (x,y,w,h) in plakalar:
        area=w*h
        if area>minArea:
            cv2.rectangle(img,(x,y),(w+w,y+h),(255,0,0),2)
            cv2.putText(img,"Plaka",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi=img[y:y+h,x:x+w] #plaka bölgesi
            cv2.imshow("ROI",imgRoi)
    
    cv2.imshow("Result",img)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Scanned/Plaka_"+current_time+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Kaydedildi",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1

    if cv2.waitKey(1) & 0xFF == ord('q'): #q basılı tutunca çalışıyor?
        break
        
    
cap.release()
cv2.destroyAllWindows()
