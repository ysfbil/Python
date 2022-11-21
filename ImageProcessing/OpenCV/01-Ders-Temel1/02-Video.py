import cv2
cap=cv2.VideoCapture("../data/vid.mp4") #http://192.168.1.25:81/stream")# #http://166.165.35.32/mjpg/video.mjpg") #

while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
