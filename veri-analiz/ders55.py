import numpy as np #veri kütüpanesi
import pandas as pd #gelişmiş veri kütüphanesi
import matplotlib as mpl #grafik kütüphanesi
import matplotlib.pyplot as plt
import seaborn as sns #gelişmiş grafik kütüphanesi
import warnings
warnings.filterwarnings("ignore") #uyarıları göstermemek için

e=pd.read_csv("50ülke.csv")
#sns.lmplot(x="BÜYÜME",y="KİŞİ BAŞINA",data=e,hue="KITA")
sns.lmplot(x="BÜYÜME",y="KİŞİ BAŞINA",data=e,col="KITA") 
plt.show()
