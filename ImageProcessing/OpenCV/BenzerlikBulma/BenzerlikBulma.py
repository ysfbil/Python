# bu yöntemle desenli 2 boyutlu resimlerin tespiti yapılabilir. kitaplar, kartlar gibi. 3 boyutlular için haar kullanmak gerekir.

import cv2
import numpy as np
 
img1 = cv2.imread('ImagesQuery/ks_album_query.jpg',0)
#img1 = cv2.imread('ImagesQuery/XBOX Kinect Sports.jpg',0)
img2 = cv2.imread('ImagesTrain/ks_album_train.jpg',0)
#img2 = cv2.imread('ImagesTrain/Kinect.jpg',0)
#img2 = cv2.imread('ImagesTrain/Last.jpg',0)
 
orb = cv2.ORB_create(nfeatures=1000) #1000: benzerlik bulunacak nokta sayısı. bu sayı arttıkça doğruluk artar. Bu değer yazılmazsa varsayılanı 500 olur.
# ORB dışında ücretli modüller de mevcuttur.

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
# imgKp1 = cv2.drawKeypoints(img1,kp1,None)
# imgKp2 = cv2.drawKeypoints(img2,kp2,None)
#des1 1000 tane 32 degerli veri içerir. Bu veriler ilgili resme ait belirleyici noktalardır.
 
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2) #k=2: altta m ve n olarak 2 boyutlu bir sonuç sağlar.
#burada knn en yakın komşuluk algoritması kullanılarak benzer noktalar bulunmuştur.

#burada knn resimlerde uyuşan noktaları ORB ile algılanan belirleyici noktalar kıysalanarak eşleştirilmektedir.

good = []
for m,n in matches:
    if m.distance < 0.75*n.distance: #eğer iki nokta arası uzaklık %75 ise listemize ekliyoruz
        good.append([m])
print(len(good))
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2) #belirlediğimiz noktalar arasında çizgi çizerek benzerlikleri tespit ediyoruz
 
# cv2.imshow('Kp1',imgKp1)
# cv2.imshow('Kp2',imgKp2)
#cv2.imshow('img1',img1)
#cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey(0)
