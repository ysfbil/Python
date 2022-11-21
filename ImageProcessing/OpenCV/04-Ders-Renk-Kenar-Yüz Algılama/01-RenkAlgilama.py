import cv2
import numpy as np

def empty(a):
    pass

path="../data/tAraba.jpg"

#max min değerleri tespit için ayar çubukları oluşturuyoruz.
cv2.namedWindow("TrackBars") #pencere oluşturduk
cv2.resizeWindow("TrackBars",640,250) #pencere boyutu
cv2.createTrackbar("Hue Min","TrackBars",0,  179,empty)
#       ayar çubuğu  başlık    pencere değer max  onchange fonksiyonu
#başlangıç değerleri
##cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
##cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
##cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
##cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
##cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

# ilk deneme sonrası güncellenen değerler
cv2.createTrackbar("Hue Max","TrackBars",24,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",55,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",211,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)


while True:
    img=cv2.imread(path)

    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #renkleri HSV yapıyoruz
    h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max=cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min=cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max=cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min=cv2.getTrackbarPos("Val Min","TrackBars")
    v_max=cv2.getTrackbarPos("Val Max","TrackBars")

    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
#sadece istenilen renk kalacak şekilde ayar yapılarak değerler not edilir
#daha sonra min, max değerleri güncllenir.
    imgResult=cv2.bitwise_and(img,  img,   mask=mask)
    #                       kaynak, hedef, maske
    
    cv2.imshow("Orjinal",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Sonuc",imgResult)
    cv2.waitKey(1) #waitKey(0) you see a still image until you actually press something
                   #waitKey(1) the function will show a frame for 1 ms only after which display will be automatically closed

    #özetle
    #cvtColor ile resmi HSV formatına çevir
    #min, max değeri tespit et
    #inRange ile maske belirle
    #bitwise_and ile resme bu maskeyi uygulayarak istenilen rengi seç
