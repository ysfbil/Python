import os
import cv2
import numpy as np

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tensorflow.python.keras.layers import Dropout, Flatten
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.utils.np_utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import ModelCheckpoint
import pickle

####################

path = 'myData'
pathLabels = 'labels.csv'
testRatio = 0.2
valRatio = 0.2
imageDimentions = (32, 32, 3)
batchSizeVal = 50
epochVal = 1  # 10 yapılacak
stepsPerEpochVal = 2000  # 2000 yapılacak
####################
count = 0
images = []
classNo = []
myList = os.listdir(path)
print("Total Classes Detected: ", len(myList))
noOfClasses = len(myList)
print("Importing classes.......")

for x in range(0, noOfClasses):
    p1 = path + "/" + str(x)
    myPicList = os.listdir(p1)
    for y in myPicList:
        p2 = p1 + "/" + y
        curImg = cv2.imread(p2)
        curImg = cv2.resize(curImg, (32, 32))
        images.append(curImg)
        classNo.append(x)
    print(x, end=" ")
print(" ")

images = np.array(images)
classNo = np.array(classNo)

# print(images.shape)
# print(classNo.shape)


####splittig data
X_train, X_test, y_train, y_test = train_test_split(images, classNo, test_size=testRatio)
X_train, X_validation, y_train, y_validation = train_test_split(images, classNo, test_size=valRatio)
print(X_train.shape)
print(X_test.shape)
print(X_validation.shape)

numOfSamples = []

for x in range(0, noOfClasses):
    numOfSamples.append(len(np.where(y_train == x)[0]))
print(numOfSamples)

plt.figure(figsize=(10, 5))
plt.bar(range(0, noOfClasses), numOfSamples)
plt.title("Her rakam için resim sayısı")
plt.xlabel("Class ID")
plt.ylabel("Number of images")
plt.show()


def preProcesssing(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255
    return img


# img=preProcesssing(X_train[3])
# img=cv2.resize(img,(300,300))
# cv2.imshow("preprocessed",img)
# cv2.waitKey(0)

X_train = np.array(list(map(preProcesssing, X_train)))
X_test = np.array(list(map(preProcesssing, X_test)))
X_validation = np.array(list(map(preProcesssing, X_validation)))

X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2],
                          1)  # tensorflow depth paremetresi de istediğinden 1 boyut daha ekliyoruz
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2], 1)
X_validation = X_validation.reshape(X_validation.shape[0], X_validation.shape[1], X_validation.shape[2], 1)

#görsellerde manipülasyon yaparak farklı datalar elde ediyoruz
dataGen=ImageDataGenerator(width_shift_range=0.1,
                           height_shift_range=0.1,
                           zoom_range=0.2,
                           shear_range=0.1,
                           rotation_range=10)
dataGen.fit(X_train)

#one hot vektöre dönüştürüyoruz
y_train=to_categorical(y_train,noOfClasses)
y_test=to_categorical(y_test,noOfClasses)
y_validation=to_categorical(y_validation,noOfClasses)

def myModel():
    noOfFilters=60
    sizeOfFilter1=(5,5)
    sizeOfFilter2=(3,3)
    sizeOfPool=(2,2)
    noOfNode=500

    model=Sequential()
    model.add((Conv2D(noOfFilters,sizeOfFilter1,input_shape=(imageDimentions[0],
                      imageDimentions[1],1), activation='relu')))
    model.add((Conv2D(noOfFilters, sizeOfFilter1, activation='relu')))
    model.add(MaxPooling2D(pool_size=sizeOfPool))
    model.add((Conv2D(noOfFilters//2, sizeOfFilter2, activation='relu')))
    model.add((Conv2D(noOfFilters//2, sizeOfFilter2, activation='relu')))
    model.add(MaxPooling2D(pool_size=sizeOfPool))
    model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(noOfNode,activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(noOfClasses, activation='softmax'))

    model.compile(Adam(0.001),loss='categorical_crossentropy',metrics=['accuracy'])
    return model


stepsPerEpochVal = len(X_train)//batchSizeVal
validation_steps = len(X_test)//batchSizeVal

model=myModel()
print(model.summary())

checkpoint_path = "training_2/cp-{epoch:04d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)


# Create a callback that saves the model's weights every 5 epochs
cp_callback = ModelCheckpoint(
    filepath=checkpoint_path,
    verbose=1,
    save_weights_only=True,
    save_freq=5*batchSizeVal)

model.save_weights(checkpoint_path.format(epoch=0))

history=model.fit_generator(dataGen.flow(X_train,y_train, batch_size=batchSizeVal),
                    steps_per_epoch=stepsPerEpochVal,
                    epochs=epochVal,
                    callbacks=[cp_callback],
                    validation_data=(X_validation,y_validation),
                    shuffle=1)

#model.save('my_model.h5')

plt.figure(1)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['training','validation'])
plt.title('loss')
plt.xlabel('epoch')

plt.figure(2)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.legend(['training','validation'])
plt.title('accuracy')
plt.xlabel('epoch')
plt.show()

score=model.evaluate(X_test,y_test,verbose=0)
print('test score:', score[0])
print('test accuracy:', score[1])

# pickle_out=open("model_trained.p","wb")
# pickle.dump(model,pickle_out)
# pickle_out.close()

