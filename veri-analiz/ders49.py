import numpy as np #veri kütüpanesi
import pandas as pd #gelişmiş veri kütüphanesi
import matplotlib as mpl #grafik kütüphanesi
import matplotlib.pyplot as plt
import seaborn as sns #gelişmiş grafik kütüphanesi
import warnings
warnings.filterwarnings("ignore") #uyarıları göstermemek için


ev=pd.read_csv("evli.csv")
sns.violinplot(x="ay",y="gelir",data=ev,hue="evli",palette="PRGn")

plt.show()
