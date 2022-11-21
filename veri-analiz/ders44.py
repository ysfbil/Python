import numpy as np #veri kütüpanesi
import pandas as pd #gelişmiş veri kütüphanesi
import matplotlib as mpl #grafik kütüphanesi
import matplotlib.pyplot as plt
import seaborn as sns #gelişmiş grafik kütüphanesi
import warnings
warnings.filterwarnings("ignore") #uyarıları göstermemek için
##
##
##e=pd.read_csv("50ülke.csv")
##sns.distplot(e["KİŞİ BAŞINA"])
##plt.show()



n=pd.read_csv("dünyam.csv")
###n.dropna(how="any",inplace=True) #bu kod ile none değerleri göz ardı etmiş oluyoruz. any tüm verileri seçmemizi sağlıyor inplace=true ile kaydetmiş olyoruz
##sns.set(style="dark",palette="muted",font_scale=2) #style=arka plan rengi ve stili (grid var v.s.), palette=renk kategorisi, font_scale=yazı boyutu
##sns.distplot(n["Doğum oranı"],bins=20,kde=False,color="g") #bins=çubuk sayısı, kde=çizgi
##plt.tight_layout()  #ekrana sığdır
##
##plt.show()

sns.set(style="darkgrid",font_scale=1.5)
f,axes=plt.subplots(2,2,figsize=(15,10)) #matplot kütüphanesinden 4lü grafik penceresi açma

sns.distplot(n["Doğum oranı"],bins=20,kde=False,color="g",ax=axes[0,0]) #axes hangi kutucuğa grafiğin çiziliceğini gösteriyor
sns.distplot(n["Yıllık değişim oranı"],hist=False,rug=True,color="r",ax=axes[0,1])
sns.distplot(n["Ortalama yaş"],hist=False,color="g",kde_kws={"shade":True},ax=axes[1,0])
sns.distplot(n["Nüfüs"],color="m",ax=axes[1,1])

plt.tight_layout()

plt.show()
