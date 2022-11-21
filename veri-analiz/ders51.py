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

#sns.barplot(x="KITA",y="KİŞİ BAŞINA",data=e,palette="RdBu_r")
sns.countplot(x="KITA",data=e,palette="RdBu_r")
plt.show()
