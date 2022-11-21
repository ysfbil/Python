import cv2
import numpy as np

wImage,hImage=480,640

cap=cv2.VideoCapture(0) #0: kamera no
cap.set(3,640) #genişlik
cap.set(4,480) #yükseklik
cap.set(10,150)#parlaklık

def empty(a):
    pass
 
cv2.namedWindow("Ayar")
cv2.resizeWindow("Ayar", 640, 240)
cv2.createTrackbar("CDeger", "Ayar", 100, 500, empty)
cv2.createTrackbar("Blur", "Ayar", 1, 20, empty)
cv2.createTrackbar("Dilate", "Ayar", 2, 10, empty)
cv2.createTrackbar("Erode", "Ayar", 1, 10, empty)

def preProcessing(img):

    cdeg = cv2.getTrackbarPos("CDeger", "Ayar")
    bdeg = cv2.getTrackbarPos("Blur", "Ayar")
    ddeg = cv2.getTrackbarPos("Dilate", "Ayar")
    edeg = cv2.getTrackbarPos("Erode", "Ayar")
    
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(5,5),bdeg)
    imgCanny=cv2.Canny(imgBlur,cdeg,cdeg)
    kernel=np.ones((5,5))
    imgDial=cv2.dilate(imgCanny,kernel,iterations=ddeg) #2 kez kalınlaştırıyoruz
    imgThres=cv2.erode(imgDial,kernel,iterations=edeg) #1 kez inceltiyoruz bu iki işlem kenarları daha belirgiln yaparak daha iyi sonuç elde etmemezi sağlıyor.

    return imgThres

def getContours(img):
    biggest=np.array([])
    maxArea=0
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
     
    for cnt in contours:
        area=cv2.contourArea(cnt)
            
        if area>5000: #büyük olan alanda işlem yapıyoruz 
            #cv2.drawContours(imgContour,cnt,       -1,      (255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.029*peri,True)
            if area>maxArea and len(approx)==4:
                biggest=approx
                maxArea = area
                #en büyük değerleri buluyoruz
    cv2.drawContours(imgContour,biggest,-1, (255,0,0),10)
    return biggest

def reorder(myPoints):
    #resmin algılanan kenar noktalarını küçükten büyüğe doğru sıralamak gerekir.
    #pts2'deki sıralamaya uygun şekilde düzenleme yapılacak
    #biggest shape yazdığımızda 4,1,2 yapısında olduğu görülür. Buradaki 1 değeri gereksizdir bu yüzden kaldırılacaktır.
    myPoints=myPoints.reshape((4,2))
    #cevap veririken sildiğimizi tekrar geri yazmamız gerekir.
    myPointsNew=np.zeros((4,1,2),np.int32)
    add=myPoints.sum(1) #köşe koordinat 2'lileri birbiriyle toplayıp (x1+x2) 4 değerli bir dize oluşturuyoruz.

    myPointsNew[0]=myPoints[np.argmin(add)]  #ilk değere toplamı en küçük olan değeri yerleştiriyoruz
    myPointsNew[3]=myPoints[np.argmax(add)] #en büyük değer sona 
    diff=np.diff(myPoints,axis=1) #koordinat farklarına bakıyoruz (x2-x1)
    myPointsNew[1]=myPoints[np.argmin(diff)] #minimum fark genişlik olarak belirleniyor
    myPointsNew[2]=myPoints[np.argmax(diff)] #maksimim fark yükseklik olarak belirlendi
    #print(myPoints)
    #print("fark",diff)
    return myPointsNew

def getWarp(img,biggest):
    biggest=reorder(biggest) #öncelikle koordinat sırasıynı pts2 değişkenindekine uygun hale getiriyoruz
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0,0],[wImage,0],[0,hImage],[wImage,hImage]])
    matrix=cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput=cv2.warpPerspective(img,matrix,(wImage,hImage))

    imgCropped=imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20] #resmimizi 20pixel her taraftan kırptık
    imgCropped=cv2.resize(imgCropped,(wImage,hImage)) #daha temiz olsun diye kırpma yapıp tekrar eski boyuta getirdik
    
    return imgCropped

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

while True:
    #success,img=cap.read()
    im=cv2.imread("../data/doc.jpg")
    img=cv2.resize(im,(wImage,hImage))
    imgContour=img.copy()
    imgThres=preProcessing(img)
    biggest = getContours(imgThres)

    if biggest.size !=0:
        imgWarped=getWarp(img,biggest)

        imageArray=([img,imgThres],
                [imgContour,imgWarped])
        cv2.imshow("Sonuc",imgWarped)
    else:
         imageArray=([img,imgThres],
                [img,img])
    

    stackedImages=stackImages(0.6,imageArray)
    
    cv2.imshow("Islemler",stackedImages)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
