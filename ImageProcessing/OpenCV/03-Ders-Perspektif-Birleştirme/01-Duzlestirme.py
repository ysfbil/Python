import cv2
import numpy as np

img=cv2.imread("../data/kartlar.png")

width,height=158,254
pts1 = np.float32([[577,282],[657,414],[363,412],[439,539]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Resim",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)
