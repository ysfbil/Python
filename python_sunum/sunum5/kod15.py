ders1=int(input("ders1:"))
ders2=int(input("ders2:"))
ders3=int(input("ders3:"))
ort=(ders1+ders2+ders3)/3
sonuc="Belge alınamadı"

if ort>=85:
    sonuc="Takdir"
elif ort>=70:
    sonuc="Teşekkür"

print("Ortalaman:",ort,sonuc)

input()