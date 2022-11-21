import numpy as np #veri kütüpanesi
import pandas as pd #gelişmiş veri kütüphanesi
import matplotlib as mpl #grafik kütüphanesi
import matplotlib.pyplot as plt
import seaborn as sns #gelişmiş grafik kütüphanesi
import warnings
warnings.filterwarnings("ignore") #uyarıları göstermemek için

enf=pd.read_csv("tüfe.csv")
enfl=enf.pivot_table(index="ay",columns="yıl",values="enflasyon") #veri tablosu oluşturuyoruz

#sns.heatmap(enfl,annot=True,linecolor="black",lw=0.5) #annot=değerleri gösterme

sns.clustermap(enfl,annot=True,figsize=(6,6)) #heatmap ten farklı olarak bağlantılı değerleri yan yana yerleştirir.
plt.show()
