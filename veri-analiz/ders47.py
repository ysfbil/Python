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

##sns.pairplot(e,hue="KITA",palette="inferno")
##
##plt.tight_layout()
##plt.show()

sns.rugplot(e["BÜYÜME"],color="y",height=0.2)
sns.kdeplot(e["BÜYÜME"],color="r")

plt.show()
