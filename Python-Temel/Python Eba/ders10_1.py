ogrenci=('yusuf','bilgen',182)
print(type(ogrenci))
print(ogrenci[2])
#ogrenci.pop(1) hata veriyor çünkü tuple da veri ekleme silme olmuyor. listenin değiştirilemeyen halidir
for bilgi in ogrenci:
	print(bilgi)
input()