
# python 3.10.4 64bit kullanınız
# pip install --upgrade gensim
# pip install pyldavis

import pandas as pd
import gensim
from gensim.corpora import Dictionary


haber_veriseti = pd.read_csv("cleaned_haber.csv")
haber_veriseti=haber_veriseti.iloc[5:35,:] #işlem kolaylığı için veriyi azalttık
#print(type(haber_veriseti["text"].iloc[3]))
tokenlastirilmis_metinler=haber_veriseti["text"].apply(lambda x: str(x).split())

#kelime listesi - dictionary oluşturma
kelime_listesi=Dictionary(tokenlastirilmis_metinler)

#kelime listesi filtreleme
kelime_listesi.filter_extremes(no_below=1,no_above=0.7)
print(kelime_listesi)
#terimlerin vektörleştirilmesi - döküman terim matrisinin oluşturulması
dokuman_terim_matrisi=[kelime_listesi.doc2bow(terim) for terim in tokenlastirilmis_metinler]

#LDA Model #burada num_topics=15 parametresi optimizasyon sonuçlarına göre alımıştır. optimizasyon işlemi en sondadır
lda_model1=gensim.models.ldamodel.LdaModel(corpus=dokuman_terim_matrisi,
                                          id2word=kelime_listesi,
                                          num_topics=15,passes=10)

#oluşturulan soyut konular içerisinde en fazla bulunan terimler
konular=lda_model1.print_topics(num_words=7)
#konular = sorted(konular,key=lambda x:x[0])
for konu in konular:
    print(konu)

#optimizasyon
    
from gensim.models import CoherenceModel


#Bu kodlar c_v kullandığı için ve bir çok konu sayısı
#için işlem yaptığından tamamlanmıyor. NOrmal bilgisayar bu işlemlerden birini bile tamamlyamıyor

#9 30 arasında 3'er atlayarak liste oluştur
konu_sayisi_aralik_listesi=range(1,50,3) 

tutarlilik_skolar_listesi=list()
konu_sayisi_listesi=list()


for konu_sayisi in konu_sayisi_aralik_listesi:
    lda_model=gensim.models.ldamodel.LdaModel(corpus=dokuman_terim_matrisi,
                                              id2word=kelime_listesi,
                                          num_topics=konu_sayisi,passes=10)
    tutarlilik_model_lda=CoherenceModel(model=lda_model,
                                        texts=tokenlastirilmis_metinler, #buna gerek yok c_v lazım
                                        dictionary=kelime_listesi,
                                        coherence='u_mass') #coherence c_v olarak seçildiğinde işlemler çok uzun sürüyor ve tamamlanamıyor. Ayrıca texts parametresi c_v için lazım
    gecici_tutarlilik_sokuru_lda=tutarlilik_model_lda.get_coherence()
    tutarlilik_skolar_listesi.append(gecici_tutarlilik_sokuru_lda)
    
    konu_sayisi_listesi.append(konu_sayisi)

import matplotlib.pyplot as plt

plt.plot(konu_sayisi_listesi,tutarlilik_skolar_listesi,"-"),
plt.xlabel("Konu Sayıları")
plt.ylabel("Tutarlılık Skorları")

plt.show()






'''
lda_model2=gensim.models.ldamodel.LdaModel(corpus=dokuman_terim_matrisi,
                                          id2word=kelime_listesi,
                                          num_topics=10,passes=10)
'''
'''

#form_models ile hesaplama

cm = CoherenceModel.for_models([lda_model1, lda_model2],
                               dictionary=kelime_listesi,
                               corpus=dokuman_terim_matrisi,
                               coherence='c_v')
'''

'''
# ayrı ayrı coherence heaplama

cm = CoherenceModel(model=lda_model1,
                               dictionary=kelime_listesi,
                               corpus=dokuman_terim_matrisi,
                               coherence='u_mass')
gecici_tutarlilik_sokuru_lda=cm.get_coherence()
print(gecici_tutarlilik_sokuru_lda)

cm = CoherenceModel(model=lda_model2,
                               dictionary=kelime_listesi,
                               corpus=dokuman_terim_matrisi,
                               coherence='u_mass')
gecici_tutarlilik_sokuru_lda=cm.get_coherence()
print(gecici_tutarlilik_sokuru_lda)

'''

