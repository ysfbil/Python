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
input()
