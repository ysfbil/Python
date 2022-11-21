'''
Girilen sayı 10 ile 100 arasında ve çift ise 
"Sayı Uygun", aksi halde "Sayı Uygun Değil" 
mesajı veren program
'''

s=int(input("Bir sayı girniz"))

if s<=100 and s>=10 and s%2==0:
    print("Sayı uygun")
else:
    print("sayı uygun değil")


input()