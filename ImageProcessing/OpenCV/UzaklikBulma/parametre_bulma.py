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

def empty(a):
    pass

cv2.namedWindow("AYAR")
cv2.resizeWindow("AYAR", 640, 240)
cv2.createTrackbar("thershold1", "AYAR", 100, 400, empty)
cv2.createTrackbar("thershold2", "AYAR", 100, 400, empty)
cv2.createTrackbar("boundary", "AYAR", 5, 40, empty)

def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                                        #      metot,          
    for cnt in contours:
        area=cv2.contourArea(cnt)
        #kenarlık alanını buluyoruz
        print("area",area)
        boundary = cv2.getTrackbarPos("boundary", "AYAR")
        
        if area>boundary: #parazitleri engellemek için sınır koyuyoruz
            cv2.drawContours(imgContour,cnt,       -1,      (255,0,0),3)
        #    kenarlık çiz  resim    kenarlık, tüm kenarlar, renk, kalınlık
            peri=cv2.arcLength(cnt,True)
            #kenarlık uzunluğunu ölçüyoruz
            print(peri)
            approx=cv2.approxPolyDP(cnt,0.029*peri,True)
            #bu işlem kenar koordinatlarını verir 0.02 deneysel bulunmuştur. 
            print("approx=",len(approx))
            x,y,w,h=cv2.boundingRect(approx)      
            print("w=",w)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)





while True:
    path='images/kumanda20cm.jpg' #shapes.png'
    img=cv2.imread(path)
    imgContour=img.copy()

    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    imgBlur = cv2.GaussianBlur(imgGray,(7,7),     1)
    #             gaus bulanıklığı      ksize     sigma

    thershold1 = cv2.getTrackbarPos("thershold1", "AYAR")
    thershold2 = cv2.getTrackbarPos("thershold2", "AYAR")
    
    imgCanny=cv2.Canny(imgBlur,thershold1,thershold2)
    #                          thershold(eşik)
    getContours(imgCanny)

    imgBlank=np.zeros_like(img)
    #boş resim

    imgStack=stackImages(0.4,([img,imgGray,imgBlur],
                              [imgCanny,imgContour,imgBlank]))

    cv2.imshow("Stack",imgStack)

   
    print("Yeni parametre denemek için bir tuşa basın. Çıkmak için q'ya basın")
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
         
cv2.destroyAllWindows()
