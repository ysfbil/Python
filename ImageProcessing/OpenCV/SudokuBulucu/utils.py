import cv2
import numpy as np
from tensorflow.python.keras.models import load_model


def preProcess(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, 1, 1, 11, 2)
    return imgThreshold


def stackImages(imgArray, scale):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        hor_con = np.concatenate(imgArray)
        ver = hor
    return ver


def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), dtype=np.int32)
    add = myPoints.sum(1)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew


def biggestContour(contours):
    biggest = np.array([])
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 50:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    return biggest, max_area


def drawRectangle(img, biggest, thickness):
    cv2.line(img, (biggest[0][0][0], biggest[0][0][1]), (biggest[1][0][0], biggest[1][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[0][0][0], biggest[0][0][1]), (biggest[2][0][0], biggest[2][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[3][0][0], biggest[3][0][1]), (biggest[2][0][0], biggest[2][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[3][0][0], biggest[3][0][1]), (biggest[1][0][0], biggest[1][0][1]), (0, 255, 0), thickness)

    return img


def splitBoxes(img):
    rows = np.vsplit(img, 9)
    boxes = []
    for r in rows:
        cols = np.hsplit(r, 9)
        for box in cols:
            boxes.append(box)
    return boxes


def initializePredictionModel():
    #klasördeki farklı modeller için test yapabilirsin
    model = load_model('Resources/my_model.h5')
    return model


# adım 4 tüm resimler için rakam tanıma tahminleri
def getPrediction(boxes, model):
    result = []
    for image in boxes:
        # resim hazırlama
        img = np.asarray(image)
        img = img[4:img.shape[0] - 4, 4:img.shape[1] - 4]
        img = cv2.resize(img, (32, 32))
        img = img / 255
        img = img.reshape(1, 32, 32, 1)

        # tahminde bulunma
        predictions = model.predict(img)
        # classIndex=model.predict_classes(img)
        classIndex = np.argmax(predictions, axis=-1)
        probabilityValue = np.amax(predictions)
        print(classIndex, probabilityValue)

        # sonuçlara kaydet
        if probabilityValue > 0.7: #burada tanıdığı rakamı kabul etme için sınır olasılık belirlendi
            result.append(classIndex[0])
        else:
            result.append(0)
    return result


## adım 4 & 5 resimde sonuçları gösterme
def displayNumbers(img, numbers, color=(0, 255, 0)):
    secW = int(img.shape[1] / 9)
    secH = int(img.shape[0] / 9)
    for x in range(0, 9):
        for y in range(0, 9):
            if numbers[(y * 9) + x] != 0:
                cv2.putText(img, str(numbers[(y * 9) + x]),
                            (x * secW + int(secW / 2) - 10, int((y + 0.8) * secH)), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                            2, color, 2, cv2.LINE_AA)

    return img

def drawGrid(img):
    secW = int(img.shape[1] / 9)
    secH = int(img.shape[0] / 9)
    for i in range(0, 9):
        pt1=(0,secH*i)
        pt2=(img.shape[1],secH*i)
        pt3=(secW*i,0)
        pt4=(secW*i,img.shape[0])
        cv2.line(img,pt1,pt2,(255,255,0),2)
        cv2.line(img, pt3, pt4, (255, 255, 0), 2)
    return img