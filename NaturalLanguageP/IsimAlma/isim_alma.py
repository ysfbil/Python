import pandas as pd
import numpy as np

liste=pd.read_csv('isimler.csv',sep=';')#,encoding = "iso-8859-9")
aciklama=liste['aciklama']

isimler=open('isimler.txt','r',encoding='utf-8').read().split()
soyisimler=open('soyisimler.txt','r',encoding='utf-8').read().split()
isim_listesi=[]
soyisim_listesi=[]
ad_soyad=[]

for ac in aciklama:
    kelimeler=ac.split()
    is_isim=False
    is_soyisim=False
    adsoyad=""
    
    for kelime in kelimeler:
      
        if kelime.upper() in isimler:
            isim_listesi.append(kelime)
            adsoyad+=kelime+' '
            is_isim=True
        elif kelime.upper() in soyisimler:
            soyisim_listesi.append(kelime)
            adsoyad+=kelime
            is_soyisim=True

    if not is_isim:
        isim_listesi.append('isimsiz')
        adsoyad+='isimsiz '
    if not is_soyisim:
        soyisim_listesi.append('soyisimsiz')
        adsoyad+='soyisimsiz '
    if is_isim and is_soyisim:
        continue;
    ad_soyad.append(adsoyad)


print(len(isim_listesi))
print(len(soyisim_listesi))
print(ad_soyad)

