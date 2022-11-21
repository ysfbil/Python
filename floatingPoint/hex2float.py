#https://www.h-schmidt.net/FloatConverter/IEEE754.html

import math

sayi = "-7.625" # input("Lütfen double sayı giriniz: ")

print("Double sayı=",sayi);

S='0' if float(sayi)>0 else '1'
print ("İşaret = ",S)

sayi_tam=abs(int(sayi.split(".")[0]))
sayi_ondalik=int(sayi.split(".")[1])

print("Tam kısım=",sayi_tam)
print("Ondalık kısım=",sayi_ondalik)

btam=bin(sayi_tam)[2:]
temp=sayi_ondalik/10**len(str(sayi_ondalik))
bondalik=""

while(temp!=1):
    temp*=2
    if (temp==0):        
        break
    elif (temp<1):
        bondalik+='0'    
    elif (temp>=1):
        bondalik+='1'
        temp-=1



print("Tam kısım bin=",btam)
print("Ondalık kısım bin=",bondalik)

us=len(btam)-1
print("Üs=",us)

E=us+127
print("float üs=",E)
bE=bin(E)[2:]
print("float bin üs=",bE)

M=btam[1:]+bondalik
print("Mantissa",M)

while len(M)<23:
    M+='0'
    
print("Uzatılmış Mantissa",M)

fpn=S+bE+M
print("Floatin Point Number=",fpn)

fpn10=int(fpn,2)
fpnHex=hex(fpn10)
print("Floatin Point HEX Number=",fpnHex)



