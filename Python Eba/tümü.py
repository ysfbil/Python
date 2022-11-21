print("selam nasilsin")
print("bir veri gir")
print(type(input()))
#bu sekilde sayi da girsen str oluyor
say1=input("bir sayı giriniz: ")
print("girdiginiz sayı: ",say1)

say2=int(input('bir sayı giriniz '))
say3=int(input('bir sayı daha lutfen '))
print('iki sayının çarpımı',say2*say3)

#--------------------------------------
hava=input("hava nasıl?")
if (hava=="yağmurlu"):
    print("şemsineyeni al")
elif (hava=="karlı"):
    print("sıkı giyin")
elif (hava=="güneşli"):
    print("kısa kol giyinebilirsin")
else:
    print("veritabanımda bu durum kayıtlı değil :(")
    
#-------------------------------
ad=input("adın nedir?")
if ad=="yusuf":
    print("adaşız", ad)
else:
    print("adaş değiliz",ad)

#---------------------------------

for degisken in range(10):
    print(degisken)
print("---")

for degisken in range(2,10): #saymaya 2 den başlıyoruz
    print(degisken)
print("---")

for i in range(1,10,3): #1 den 9a kadar 3er 3er say
    print(i)
print("---")

t=0
for i in range(1,51):
    t+=i
print(t)

#----------------------------------------------

toplam=0
for n in range(1,6):
    sayi=int(input(str(n)+" . dersin notunu giriniz:"))
    toplam+=sayi
print("ortalamanız:",toplam/5)

#----------------------------------------------

sayi=0
while(sayi!=8):
    sayi=int(input("1-10 arasında sayımı tahmin ediniz"))
    print("tekrar dene...")
print("tebrikler")

#------------------------------------------------------

metin="bilgen"
print(metin[0:3])
for harf in metin:
	print(harf)
print(len(metin))
print(metin[::-1])
print(metin[2:0:-1])
print(metin[1])

#--------------------------

ogrenci=['yusuf','bilgen',182]
print(type(ogrenci))
print(ogrenci)
print("ögrencinin nosu",ogrenci[2])
ogrenci.append("imam hatip")
ogrenci.pop(1)
for bilgi in ogrenci:
	print(bilgi)
	
#------------------------------------------

ogrenci=('yusuf','bilgen',182)
print(type(ogrenci))
print(ogrenci[2])
#ogrenci.pop(1) hata veriyor çünkü tuple da veri ekleme silme olmuyor. listenin değiştirilemeyen halidir
for bilgi in ogrenci:
	print(bilgi)
	
#-------------------------------------------

#() tuple [] list {} dictionary
sozluk={"araba":"car","kırmızı":"red"}
print(sozluk)
print(sozluk["araba"])
print(sozluk["kırmızı"])

for kelime in sozluk:
    print(kelime+" ingilizcesi: "+sozluk[kelime])

#---------------------------------------------

from time import * #clock yazarsak sadece o kısmı import etmiş oluşuruz. import time ile de tümü import edilebilir

t1=perf_counter()
input('Adınız')
t2=perf_counter()
print((t2-t1),'kadar süre geçti')

#-----------------------------------------------------

from time import *
a=input('adınız')
sleep(2)
b=input('soyad')
print(a+b)

#-----------------------------------------------

def mesaj():
	print('selam')
	print('yusuf')
	
def kare(a):
	return a**2
	
def tamad(isim,soyisim):
	return isim+" "+soyisim

mesaj()
s=int(input('sayı giriniz'))
print(kare(s))

a=input('ad:')
b=input('soyad:')
print(tamad(a,b))

#----------------------------------

def belge(notlar):
	ort=0
	s=0
	
	for n in notlar:
		ort+=n
		s+=1
	ort=ort/s
	
	if ort>84.99:
		return  'Takdir Ort:'+str(ort)
	elif ort>=70:
		return 'Teşekkür Ort:'+str(ort)
	else:
		return 'Belge alamadınız Ort:'+str(ort)
		
notum=[]
g=0

print('Notlarınızı giriniz/Girişi tamamlamak için -1 giriniz.')
while(g>-1):
	g=int(input('Not:'))
	if g>-1:
		 notum.append(g)
		
print(belge(notum))

#------------------------------------------

dosya=open("ders15.txt",encoding="utf-8") #varsayılan mode='r' yani okumadır. 
print("1. satır:"+dosya.readline()) #tek bir satır okuyoruz
print(dosya.read()) #tüm dosyayı okuyoruz
dosya.close()
dosya2=open("ders15.txt",mode="a",encoding="utf-8") #append dosya yoksa oluşturuyor, varsa ekleme yaptırıyor
dosya2.write("\nnasılsın yusuf abi")
dosya2.close()
dosya=open("ders15.txt",encoding="utf-8") #varsayılan mode='r' yani okumadır. 
print(dosya.read()) 
dosya.close()

#------------------------------------------

input()