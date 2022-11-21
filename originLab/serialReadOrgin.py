import serial
import time

print("Arduino'ya atiniz")
comp="COM5"
numPoints=100
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
