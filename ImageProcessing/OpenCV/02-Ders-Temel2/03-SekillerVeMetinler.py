import cv2
import numpy as np

#img=np.zeros((512,512)) #512,512 boyutunda siyah,beyaz kanallı boş resim oluşturduk
img = np.zeros((512,512,3),np.uint8) #512x512 boyutunda,BGR kanallı boş resim
print(img.shape)

img[:]=255,0,0 #tüm resmi mavi yap
img[200:300,100:300]=0,0,255 #belirtilen bölüme kırmızı  yap

yukseklik=img.shape[0]
genislik=img.shape[1]

cv2.line(img,(0,0),(genislik,yukseklik),(0,255,0),3)
#             baş   bitiş                renk    kalınlık

cv2.rectangle(img,(0,0),(250,350),(0,0,0),2)
#   dikdörtgen     baş   bitiş     renk   çizgi kalınlığı

cv2.rectangle(img,(250,350),(400,500),(0,0,0),cv2.FILLED)
#                                             içi dolu

cv2.circle(img,(400,50),30,(255,255,0),5)
#   çember      merkez  çap  renk      kalınlık

cv2.putText(img,"Yusuf Bilgen ile Ahmet Yasin",(3,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
#    yazı        metin                          başlangıç,  yazı tipi,    yazı boyutu, yazı rengi, kalınlık         
cv2.imshow("REsim",img)

cv2.waitKey(0)
