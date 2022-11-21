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

#sns.boxplot(x="KITA",y="BÜYÜME",data=e)

ev=pd.read_csv("evli.csv")
sns.boxplot(x="ay",y="gelir",data=ev,hue="evli",palette="PRGn")

plt.show()
