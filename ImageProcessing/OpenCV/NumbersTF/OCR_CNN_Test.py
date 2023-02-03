import numpy as np
import cv2
from tensorflow.keras.models import  load_model
# from OCR_CNN_Training import preProcesssing
import pickle

width = 640
height = 480
thershold = 0.65

cap = cv2.VideoCapture(1)
cap.set(3, width)
cap.set(4, height)

# pickle_in = open("model_trained.p", "rb")
# model = pickle.load(pickle_in)
model=load_model('my_model.h5')

def preProcesssing(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255
    return img


while True:
    success, imgOriginal = cap.read()
    img = np.asarray(imgOriginal)
    img = cv2.resize(img, (32, 32))
    img = preProcesssing(img)
    cv2.imshow("processed image", img)
    img = img.reshape(1, 32, 32, 1)

    # predict
    classIndex = int(model.predict_classes(img))
    predictions = model.predict(img)
    probVal = np.amax(predictions)
    print(classIndex, probVal)
    if probVal > thershold:
        cv2.putText(imgOriginal, str(classIndex) + " " + str(probVal),
                    (50, 50), cv2.FONT_HERSHEY_COMPLEX,
                    1, (0, 0, 255), 1)
    cv2.imshow("Orjinal",imgOriginal)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

