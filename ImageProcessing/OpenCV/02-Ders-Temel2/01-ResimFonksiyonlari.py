import cv2
import numpy as np

kernel=np.ones((5,5),np.uint8) #5x5'lik 1'lerden oluşan ve 0-255 arası değer alabilen bir matris oluşturuyoruz
img=cv2.imread("../data/res.jpg")

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(img,(7,7),0) #sayılar bulanıklık oranıdır
imgCanny=cv2.Canny(img,150,200) #sayıları büyütünce çizgi sayısı azalır
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1) #Çizdiğimiz kenarı böylece kalılanştırabiliriz. iterations çizgi kalınlığını değiştirir
imgEroded=cv2.erode(imgDialation,kernel,iterations=1) #Çizgi kalınlığında erozyon, aşındırma yapar.

cv2.imshow("Gri Resim",imgGray)
cv2.imshow("Bulanik Resim",imgBlur)
cv2.imshow("Resim Hatlari",imgCanny)
cv2.imshow("Kalin Resim Hatlari",imgDialation)
cv2.imshow("Asindirilmis Resim Hatlari",imgEroded)

cv2.waitKey(0)
