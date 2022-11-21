say1=float(input("1. Sayı: "))
say2=float(input("2. Sayı: "))
say3=float(input("3. Sayı: "))
enbuyuk=say3

if say1>say2:
    if say1>say3:
        enbuyuk=say1
elif say2>say3:
    enbuyuk=say2

print("En büyük",enbuyuk)

input()