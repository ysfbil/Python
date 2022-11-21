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

#sns.factorplot(x="KITA",y="BÜYÜME",data=e,kind="violin") #kind=point v.s yapılarak farklı grafik türleri elde edilebilir.

t=pd.read_csv("titanic.csv") #,dtype={'Survived': np.int32,'Pclass': np.int32,'Age': 'Int64','Siblings/Spouses Aboard': np.int32,'Parents/Children Aboard': np.int32,'Fare':np.float64})
sns.factorplot(x="Pclass",y="Survived",hue="Sex",data=t,kind="violin",palette="muted")
plt.show()
