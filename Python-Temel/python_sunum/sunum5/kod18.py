'''
Bir firma aşağıdaki tabloya göre bir indirim tarifesi uyguluyor.
Öğrenci : %20
Öğretmen: %5
60 yaş üstü:%15
Engelli: %30

Bir kişi sadece tekbir indirimden yararlanabilmektedir.
Kişinin yararlanabileceği enbüyük indirim uygulanır.
Bu bilgileri ve ürün fiyatını kullanıcıdan alarak ilgili indirim
yapan ve ödenecek tutarı ekrana yazan bir uygulama yazalım.
'''

meslek=input("Mesleğiniz: ").lower()
yas=int(input("Yaşınız: "))
engel=input("Engel durumu var/yok: ")=="var"
fiyat=float(input("Ürün fiyatı: "))

if engel:
    sonuc=fiyat-fiyat*0.3
elif meslek=="öğrenci":
    sonuc=fiyat-fiyat*0.20
elif yas>=60:
    sonuc=fiyat-fiyat*0.15
elif meslek=="öğretmen":
    sonuc=fiyat-fiyat*0.05
else:
    sonuc=fiyat

print("Ödeyeceğiniz tutar=",sonuc)

input()