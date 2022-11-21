# python 3.10.4 64bit kullanınız
# pip install --upgrade gensim
# pip install pyldavis

import numpy as np
import pandas as pd
df=pd.read_csv("turkish_news_lite.csv",index_col="id")
print(df.head(3))

#LDA için text sütunu verisi yeterlidir
haber_veriseti=df[["text"]]
print(haber_veriseti.head(3))

#veri temizleme
import re
import string
import nltk
from nltk.corpus import stopwords
#import csv

nok_isaretleri_kumesi=string.punctuation
etkisiz_kelimeler_kumesi=stopwords.words("turkish")

etkisiz_kelimeler_kumesi.extend(["bir","kadar","sonra","iframe","www","com","haber","tarih","detay","haberler","içerikler","olay","tarafından","nedeniyle","ilgili","yeni","önemli","olarak","var","değil","iyi","yüzde","milyon","bin","milyar","göre","şekilde","hakkında","yıl","olduğu","başkanı","son","lira","fazla","olan","endeksi","ilk","ben","büyük","yeni"])

def veri_temizleme(metin):
    metin=metin.lower()
    #yen satır ve boşluk kaldırma
    metin=metin.replace("\\n"," ")
    #kesme işareti ve sonrasındaki karakterleri kaldırma
    metin=re.sub("'(\w+)","",metin)
    metin=re.sub("‘(\w+)","",metin)
    metin=re.sub("[“,’,‘,”]","",metin)
    #sayıların kaldırılması
    metin=re.sub("[0-9]+","",metin)
    #noktalaam işaretlerinin kaldırılması
    metin="".join(list(map(lambda x:x if x not in nok_isaretleri_kumesi else " ",metin)))
    #etkisiz kelimleri kaldırma
    metin=" ".join([i for i in metin.split() if i not in etkisiz_kelimeler_kumesi])
    #metinde tek kalan harfleri de çıkarma
    metin=" ".join([i for i in metin.split() if len(i)>1])

    return metin

#haber_veriseti.insert(0,"text_temiz",haber_veriseti["text"].apply(veri_temizleme))
#ayrı bir sütun olarak temizlenmiş veriyi kaydetmek için yukarıdaki kodu kullanınız

haber_veriseti["text"]=haber_veriseti["text"].apply(veri_temizleme)

#print(haber_veriseti["text_temiz"].head())

#bu şekilde yapınca uyarı veriyor yukarıdaki gibi yapılınca uyarısız oluyor
# haber_veriseti["text_temiz_token"]=haber_veriseti["text_temiz"].apply(lambda x: x.split())
# token kaydedip sonra çağrıldığında birçok temizleme işlemi gerekiyor. csv dosyası da boşuna şişiyor. Bu sebeple iptal ettik. lda kısmında oluşturulacak
# print(haber_veriseti["text_temiz_token"].head())

haber_veriseti.to_csv(r'cleaned_haber.csv',index=False)
# haber_veriseti.to_csv(r'cleaned_haber.csv',index=False,sep="\t", quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\")
# csv formatını farklılşatırmak için yukardaki satır kullanılır. import csv'nin de açılması gerekir

print("tamamlandı")

#lda algoritması # ayrı dosyaya taşındı
'''
import pandas as pd
import gensim
from gensim.corpora import Dictionary
#import pyLDAvis #LDA konu modelmesi figürsel gösterimi için


tokenlastirilmis_metinler=haber_veriseti["text_temiz_token"]

#kelime listesi - dictionary oluşturma
kelime_listesi=gensim.corpora.Dictionary(tokenlastirilmis_metinler)

#kelime listesi filtreleme
kelime_listesi.filter_extremes(no_below=1,no_above=0.7)
print(kelime_listesi)
#terimlerin vektörleştirilmesi - döküman terim matrisinin oluşturulması
dokuman_terim_matrisi=[kelime_listesi.doc2bow(terim) for terim in tokenlastirilmis_metinler]

#LDA Model
lda_model=gensim.models.ldamodel.LdaModel(corpus=dokuman_terim_matrisi,
                                          id2word=kelime_listesi,
                                          num_topics=15,passes=10)

#oluşturulan soyut konular içerisinde en fazla bulunan terimler
konular=lda_model.print_topics(num_words=7)

for konu in konular:
    print(konu)

#optimizasyon
    
from gensim.models import CoherenceModel

#9 30 arasında 3'er atlayarak liste oluştur
konu_sayisi_aralik_listesi=range(9,30,3) 

tutarlilik_skolar_listesi=list()
konu_sayisi_listesi=list()

for konu_sayisi in konu_sayisi_aralik_listesi:
    lda_model=gensim.models.ldamodel.LdaModel(corpus=dokuman_terim_matrisi,
                                              id2word=kelime_listesi,
                                          num_topics=konu_sayisi,passes=10)
    tutarlilik_model_lda=CoherenceModel(model=lda_model,
                                        texts=tokenlastirilmis_metinler,
                                        dictionary=kelime_listesi,
                                        coherence='c_v')
    gecici_tutarlilik_sokuru_lda=tutarlilik_model_lda.get_coherence()
    tutarlilik_skolar_listesi.append(gecici_tutarlilik_sokuru_lda)
    konu_sayisi_listesi.append(konu_sayisi)

import matplotlib.pyplot as plt

plt.plot(konu_sayisi_listesi,tutarlilik_skolar_listesi,"-"),
plt.xlable("Konu Sayıları")
plt.ylabel("Tutarlılık Skorları")

plt.show()
'''
                                        
