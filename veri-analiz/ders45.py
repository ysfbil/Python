import numpy as np #veri kütüpanesi
import pandas as pd #gelişmiş veri kütüphanesi
import matplotlib as mpl #grafik kütüphanesi
import matplotlib.pyplot as plt
import seaborn as sns #gelişmiş grafik kütüphanesi
import warnings
warnings.filterwarnings("ignore") #uyarıları göstermemek için

n=pd.read_csv("dünyam.csv")
sns.jointplot(n["Doğum oranı"],n["Ortalama yaş"],data=n)
sns.jointplot(n["Yıllık değişim oranı"],n["Doğum oranı"],data=n,kind="kde",xlim=(-2,6),ylim=(0,10),color="r",size=8)
plt.show()
