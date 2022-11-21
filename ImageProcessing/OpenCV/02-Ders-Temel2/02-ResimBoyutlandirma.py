import cv2
img=cv2.imread("../data/res.jpg")
print(img.shape) #resmin sırasıyla yükseklik, genişlik ve kanalı gösterir. kanal=3 BGR anlamına gelir.

imgResize=cv2.resize(img,(150,200))
print(imgResize.shape)

imgCropped=img[0:100,30:150]

cv2.imshow("Resim",img)
cv2.imshow("Boyulandirilmis Resim",imgResize)
cv2.imshow("Kirpilmis resim",imgCropped)

cv2.waitKey(0)
