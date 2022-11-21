#https://www.pyimagesearch.com/2015/01/19/find-distance-camera-objectmarker-using-python-opencv/#pyis-cta-modal

from imutils import paths
import numpy as np
import cv2
import imutils
thershold1=100
thershold2=100

def find_marker(image):
        minArea=0.0
        imgGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray,(7,7),     1)
        #             gaus bulanıklığı      ksize     sigma

        imgCanny=cv2.Canny(imgBlur,thershold1,thershold2)
        #                          thershold(eşik)

        contours,hierarchy=cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                                        #      metot,          
        for cnt in contours:
                area=cv2.contourArea(cnt)
                #kenarlık alanını buluyoruz
                #print("area",area)
                boundary = 5

                if area>boundary: #parazitleri engellemek için sınır koyuyoruz
                    #cv2.drawContours(image,cnt,       -1,      (255,0,0),3)
                    #kenarlık çiz  resim    kenarlık, tüm kenarlar, renk, kalınlık
                    peri=cv2.arcLength(cnt,True)
                    #kenarlık uzunluğunu ölçüyoruz
                    print(peri)
                    approx=cv2.approxPolyDP(cnt,0.029*peri,True)
                    #bu işlem kenar koordinatlarını verir 0.02 deneysel bulunmuştur. 
                    print("approx=",len(approx))
                    x,y,w,h=cv2.boundingRect(approx)      
                                      
                    marker = cv2.minAreaRect(cnt)[1][0] #en küçük dikdörtgen dönmüş dikdörtgeni de bulur.
                    minArea=w

                    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

        return minArea

def distance_to_camera(knownWidth, focalLength, perWidth):
	# compute and return the distance from the maker to the camera
	return (knownWidth * focalLength) / perWidth

# initialize the known distance from the camera to the object, which
# in this case is 40 cm
KNOWN_DISTANCE =40.0
# initialize the known object width, which in this case, the piece of
# 4.5cm wide
KNOWN_WIDTH = 4.5
# load the furst image that contains an object that is KNOWN TO BE 2 feet
# from our camera, then find the paper marker in the image, and initialize
# the focal length
image = cv2.imread("images/kumanda40cm.jpg")
marker = find_marker(image)
focalLength = (marker * KNOWN_DISTANCE) / KNOWN_WIDTH
print("focalLength=",focalLength)
# loop over the images


for imagePath in sorted(paths.list_images("images")):

    image = cv2.imread(imagePath)
    
    marker = find_marker(image)
    santim = distance_to_camera(KNOWN_WIDTH, focalLength, marker)
   
    cv2.putText(image, "%.2fcm" % (santim),
                (image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (0, 255, 0), 3)
    cv2.namedWindow("image")
    cv2.moveWindow("image", 40,30)
    cv2.imshow("image", image)

    print("Devam etmek için bir tuşa basınız. Çıkmak için q'ya basınız")

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
