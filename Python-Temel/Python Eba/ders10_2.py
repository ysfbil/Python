#() tuple [] list {} dictionary
sozluk={"araba":"car","kırmızı":"red"}
print(sozluk)
print(sozluk["araba"])
print(sozluk["kırmızı"])

for kelime in sozluk:
    print(kelime+" ingilizcesi: "+sozluk[kelime])
input()