import random

sayi=0
sabit=random.randrange(1,50)

while(sayi!=sabit):
    sayi=int(input("1-50 arasında sayımı tahmin ediniz"))
    if sayi>sabit:
        print("aşağı")
    elif sayi<sabit:
        print("yukarı")
print("tebrikler")
input()
