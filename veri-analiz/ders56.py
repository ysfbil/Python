import numpy as np #veri kütüpanesi
import pandas as pd #gelişmiş veri kütüphanesi
import matplotlib as mpl #grafik kütüphanesi
import matplotlib.pyplot as plt
import seaborn as sns #gelişmiş grafik kütüphanesi
import warnings
warnings.filterwarnings("ignore") #uyarıları göstermemek için

e=pd.read_csv("50ülke.csv")
e.pop("2023") #pop ile istemediğmiz sütunları çıkarıyoruz
e.pop("SIRALAMA")
e.pop("SIRALAMA.2")

##m=sns.PairGrid(e) #tüm veriler için grafik oluşturuyor
##m.map_diag(sns.distplot)
##m.map_upper(plt.scatter)
##m.map_lower(sns.kdeplot)

s=pd.read_csv("evli.csv")
ss=sns.FacetGrid(data=s,col="ay",row="evli")
ss.map(sns.distplot,"gelir")
plt.show()
