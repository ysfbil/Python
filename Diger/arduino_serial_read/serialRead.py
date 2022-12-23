#pip install pySerial #ile kütüphaneyi yüklüyoruz
import serial
import time
import matplotlib.pyplot as plt

print("Arduino'ya reset atınız!")
comp="COM"+input("COM portunu giriniz (1,2,3...)")
numPoints=int(input("istenilen data sayısını giriniz"))
ser = serial.Serial(comp, baudrate = 9600, timeout = 1)
time.sleep(3)
dataList = [0]*numPoints

def getValues():
    
    arduinoData = ser.readline().decode().split('\r\n')
    
    return arduinoData[0]

tekrar=False;

while(not tekrar):

    for i in range(0,numPoints):
        data = getValues()
        data = int(data)
        dataList[i] = data

            
    dataAvg = sum(dataList)/numPoints
    print("Ortalama=",dataAvg)

    tekrar=input("Tekrar veri toplansın mı? (e/h)")=='h'
    if (tekrar):
        print("Grafik çiziliyor")
        x_val =range(numPoints)
        plt.xlabel("x ekseni")
        plt.ylabel("Arduino verisi")
        plt.scatter(x_val,dataList)
        plt.show()


