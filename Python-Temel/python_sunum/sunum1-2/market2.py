#daha sonra proje ödevi olarak verilecek

buyukPaket,ortaPaket,kucukPaket,tekli=0,0,0,0

misafirSayisi=int(input("Misafir sayısını giriniz:"))

if (misafirSayisi>=40):
    buyukPaket = int(misafirSayisi/40)
    misafirSayisi=misafirSayisi-buyukPaket*40

if (misafirSayisi>=20):
    ortaPaket=int(misafirSayisi/20)
    misafirSayisi=misafirSayisi-ortaPaket*20

if (misafirSayisi>=10):
    kucukPaket=int(misafirSayisi/10)
    misafirSayisi=misafirSayisi-kucukPaket*10

if (misafirSayisi>0):
    tekli=misafirSayisi
        
toplamOdenen=buyukPaket*6+ortaPaket*3.5+kucukPaket*2+tekli*0.25
print(buyukPaket," adet büyük paket, ",ortaPaket," adet orta paket, ",
      kucukPaket, " adet küçük paket, ",tekli,
      " adet tekli paket alınması gerekiyor")
print("Toplam ödenecek tutar: ",toplamOdenen)

input()





