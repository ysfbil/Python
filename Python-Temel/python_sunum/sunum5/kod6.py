'''
Girilen sayı hem 4 hem 5, hem de 6 ile 
bölünebiliyorsa "Sayı Uygun”, aksi halde 
"Sayı Uygun Değil" mesajı veren program
'''

s=int(input("bir sayı giriniz"))

if s%4==0 and s%5==0 and s%6==0:
    print("Sayı uygun")
else:
    print("Sayı uygun değil")

input()