#Lale ebru resmini tanıyacak şekilde eğitildi. 3 boyutlu resimler için eğitmek daha zor oluyor.

## Not: Sanırım az resimle eğitim yaptırdığımızdan yeterince verimli çalışmıyor. Resim sayısı arttırılarak verim arttırılabilir. Negatif resim sayısı pozitifin en az 5 katı olsun. Negatif resimler çok alakasız olmasın.
## resimlerin boyutlarını ve formatlarını aynı yapıp işlem yap. eğitim programında ( Cascade-Trainer-GUI ) width height oranını resim boyutlarındaki ile aynı ayarla. Örneğin 180x120 resimler için eğitim programında da width 36 height 24 olarak girilebilir. 180/120=36/24

#sonuç seçtiğim resimler çok uygun olmadığı için 1000 lik negatif data ile yaptığım eğitim 220'lik negatif data verisinden daha kötü bir sonuç verdi. Eğitim resimleri çok önemli. Nesnenin tamamını kadraja almak ve farklı arka planlar ve açılardan resimlerini çekmek daha iyi sonuç verecektir. Negatif resimler için ise benzer nesnelerin fotoğraflarını yüklemek gerekir. Bilgisayarın hangi resimleri benzer kabul ettiğini anlamak için daha az veri ile bir eğitim yapıp test ederek bilgisayarın karıştırdığı nesneleri tespit etmek ve bu resimleri özellikle negatif olarak eklemek olumlu sonuç verecektir kanaatindeyim. Her zaman çok resim daha iyi sonuç vermiyor çok ve doğru resimler ile eğitmek önemli.

import cv2
 
################################################################
path = '../data/haarcascades/haarcascade_lale.xml' #haarcascade_trex211n.xml' #haarcascade_trex1000n.xml'  # PATH OF THE CASCADE
cameraNo = 0                       # CAMERA NUMBER
objectName = 'Lale'       # OBJECT NAME TO DISPLAY
frameWidth= 640                     # DISPLAY WIDTH
frameHeight = 480                  # DISPLAY HEIGHT
color= (255,0,255)
#################################################################
 
 
cap = cv2.VideoCapture(cameraNo)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
 
def empty(a):
    pass
 
# CREATE TRACKBAR
cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",120,1000,empty)
cv2.createTrackbar("Neig","Result",20,50,empty)
cv2.createTrackbar("Min Area","Result",5400,100000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)
 
# LOAD THE CLASSIFIERS DOWNLOADED
cascade = cv2.CascadeClassifier(path)
 
while True:
    # SET CAMERA BRIGHTNESS FROM TRACKBAR VALUE
    cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    cap.set(10, cameraBrightness)
    # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # DETECT THE OBJECT USING THE CASCADE
    scaleVal =1 + (cv2.getTrackbarPos("Scale", "Result") /1000)
    neig=cv2.getTrackbarPos("Neig", "Result")
    objects = cascade.detectMultiScale(gray,scaleVal, neig)
    # DISPLAY THE DETECTED OBJECTS
    for (x,y,w,h) in objects:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        if area >minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            roi_color = img[y:y+h, x:x+w]
 
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
