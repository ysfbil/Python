'''
ikinci derece denklem köklerinin bulunması

ax^2+bx+c=0  şeklinde verilen denklemimiz için;
D=b**2-4*a*c
ile delta hesaplanır
D<0 ise reel kök yok
D=0 ise iki kök birbirine eşit
D>0 ise iki farklı reel kök var
Kullanıcıdan a,b,c değerlerini isteyelim
Deltayı hesaplayıp kökük durumunu ekrana yazdıralım ve reellik durumunu
bir değişkende tutalım.
daha sonra reel kök varsa kullanıcıya çözümü istiryor musun diye soralım
e/h seçeneklerinden e seçilirse
(-b+kök(D))/2a
(-b-kök(D))/2a
formülleri ile kökleri ekrana yazdırılaım.
'''
import math

print('ax^2+bx+c=0 şeklinde verilen denklemimiz için a,b,c değerlerini giriniz?')
a=float(input('a değeri='))
b=float(input('b değeri='))
c=float(input('c değeri='))
D=b**2-4*a*c
reel=False

if D>0:
    mesaj='İki farklı reel kök mevcut'
    reel=True
elif D==0:
    mesaj='Tekbir reel kök mevcut'
    reel=True
else:
    mesaj='Reel kök yok'
    reel=False

print(mesaj)

if reel:
    yanit=input("Kökleri görmek istiyor musunuz e/h")
    if yanit=='e':
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        print("1. kök x1=",x1)
        print("2. kök x2=",x2)
    
input()
