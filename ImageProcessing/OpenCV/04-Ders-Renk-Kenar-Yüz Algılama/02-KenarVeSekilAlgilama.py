import cv2
import numpy as np

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

def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
                                        #      metot,          
    for cnt in contours:
        area=cv2.contourArea(cnt)
        #kenarlık alanını buluyoruz
        print(area)
        if area>500: #parazitleri engellemek için sınır koyuyoruz
            cv2.drawContours(imgContour,cnt,       -1,      (255,0,0),3)
        #    kenarlık çiz  resim    kenarlık, tüm kenarlar, renk, kalınlık
            peri=cv2.arcLength(cnt,True)
            #kenarlık uzunluğunu ölçüyoruz
            print(peri)
            approx=cv2.approxPolyDP(cnt,0.029*peri,True)
            #bu işlem kenar koordinatlarını verir 0.02 deneysel bulunmuştur. 
            print(len(approx))
            objCor=len(approx) #kenar koordinat sayısı şeklin kaç kenarlı olduğunu verir
            x,y,w,h=cv2.boundingRect(approx)
            #Çerçeve oluşturuyoruz.

            if objCor==3:objectType="3gen"
            elif objCor==4:
                aspRatio=w/float(h)
                if aspRatio>0.95 and aspRatio<1.05:objectType="Kare"
                else:objectType="4Gen"
            elif objCor==5: objectType="5Gen"
            elif objCor==6: objectType="6Gen"
            elif objCor==7: objectType="7Gen"
            elif objCor==8: objectType="8Gen"
            elif objCor==9: objectType="9Gen"
            elif objCor==10: objectType="10Gen"
            elif objCor>10: objectType="Daire"
            else:objectType="Unknown"
        

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            # dikdörtgen   resim      baş   son       renk    kalınlık
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)

path='../data/sekiller.jpg' #shapes.png'
img=cv2.imread(path)
imgContour=img.copy()

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),     1)
#             gaus bulanıklığı      ksize     sigma
imgCanny=cv2.Canny(imgBlur,50,50)
#                          thershold(eşik)
getContours(imgCanny)

imgBlank=np.zeros_like(img)
#boş resim

imgStack=stackImages(0.8,([img,imgGray,imgBlur],
                          [imgCanny,imgContour,imgBlank]))

cv2.imshow("Stack",imgStack)

cv2.waitKey(0)
