'''
Girilen sayı 4, 5 ve 6 sayılarından en az 
birine bölünüyorsa "Sayı Uygun", aksi halde 
"Sayı Uygun Değil" mesajı veren program
'''

s=int(input("bir sayı giriniz"))

if s%4==0 or s%5==0 or s%6==0:
    print("Sayı uygun")
else:
    print("Sayı uygun değil")

input()