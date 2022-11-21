# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 17:00:03 2022
Tek parametreli çözüm
@author: fizik
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
hamveri=pd.read_csv('datas/maaslar_yeni.csv')
print(hamveri.corr())
#korelasyonlara baktığımızda Kidem ve Puan'ın düşük etkisi var.
#statsmodel api ile de ilişki anlaşılabiir
veri=hamveri.drop(['Calisan ID','unvan','Kidem'],axis=1)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
y=veri.iloc[:,-1]
x=veri.iloc[:,:-1]
lr=lr.fit(x,y)
y_p=lr.predict(x)
ud=x.iloc[:,:1]
print(hamveri)
'''
#zayıf ilişkiyi grafikler ile de görebiliriz.
#x_ekseni=hamveri.sort_values(by=[grafik_basligi])
plt.title('Unvan Seviyesi')
plt.scatter([hamveri['UnvanSeviyesi']],y,color='blue')
plt.show() #yazılmazsa aynı grafikte gösterilirler
plt.title('Kıdem')
plt.scatter([hamveri['Kidem']],y,color='red')
plt.show()
plt.title('Paun')
plt.scatter([hamveri['Puan']],y,color='green')
#plt.scatter(ud,y_p,color='red')
plt.show()'''

sl=r2_score(y, y_p)
print('Lineer Reg. R2 Score',sl)

from sklearn.preprocessing import PolynomialFeatures
pf=PolynomialFeatures(degree=2)
xp=pf.fit_transform(x.values)
lrp=LinearRegression()
lrp=lrp.fit(xp,y)
y_pp=lrp.predict(xp)
sp=r2_score(y,y_pp)
print('Polynomial R2 Score',sp)

from sklearn.svm import SVR
sr=SVR(kernel='rbf')
from sklearn.preprocessing import StandardScaler
scl=StandardScaler()
xf=scl.fit_transform(x.values)
scl=StandardScaler()
yf=scl.fit_transform(y.values.reshape(-1,1)) #reshape ile 2 boyuta çevirdik (transform öyle istiyor)
yf=np.ravel(yf) #ravel ile düzleştirip tekrar 1 boyutlu yaptık (fit öyle istiyor)
lssv=sr.fit(xf, yf)
yps=lssv.predict(xf)
ssr=r2_score(yf,yps)
print('SVM R2 Score',ssr)

from sklearn.tree import DecisionTreeRegressor
dtr=DecisionTreeRegressor()
ldtr=dtr.fit(x,y)
ydt=ldtr.predict(x)
sdtr=r2_score(y,ydt)
print('Decision Tree R2 Score',sdtr)

from sklearn.ensemble import RandomForestRegressor
rfr=RandomForestRegressor()
rfr.fit(x,y)
yrfr=rfr.predict(x)
srfr=r2_score(y,yrfr)
print('Random Forest R2 Score',srfr)


x_test10=[[10,100],[7,100]] #ceo 10 ,mudur 7 100 puan almış 9 kıdemili müdür ve ceo maaşları
x_test10=pd.DataFrame(data=x_test10,columns=['UnvanSeviyesi','Puan'])


y_p=lr.predict(x_test10) #lineer

xp=pf.fit_transform(x_test10)
y_pp=lrp.predict(xp) #polynom

scl2=StandardScaler() #simple vector regressor
xf=scl2.fit_transform(x_test10)
yps=lssv.predict(xf)
yps=scl.inverse_transform(yps.reshape(-1,1))

ydt=ldtr.predict(x_test10)

yrfr=rfr.predict(x_test10)
yontem=pd.DataFrame(data=['Lineer','Polynomial','Simple Vector Regressor','Decision Tree','Random Forest Regressor'],columns=['Yöntem'])
sonuc1=pd.DataFrame(data=np.round([y_p,y_pp,np.ravel(yps),ydt,yrfr],decimals=0),columns=['10 Yıllık CEO','10 Yıllık Müdür'])
sonuc=pd.concat([yontem,sonuc1],axis=1)
print(sonuc)

'''
#tablo incelendiğinde 10 yıllık ceo'nun 60bin civarı, 10 yıllık müdürün ise 12bin civarı alması mantıklı 
#durmaktadır. Sonuçlara baktığımızda bu değeri 2 parametreli random forest en doğru şekilde tahmin etmiştir. Decision Tree ise ezbere davrandığı için güvenilir değildir.


#sadece ünvan sırası ile
Lineer Reg. R2 Score 0.5285811733746243
Polynomial R2 Score 0.724408921062337
SVM R2 Score 0.5841869084594333
Decision Tree R2 Score 0.8343186200100907
Random Forest R2 Score 0.8240174342456893
                    Yöntem  10 Yıllık CEO  10 Yıllık Müdür
0                   Lineer        25945.0          15889.0
1               Polynomial        35622.0          11051.0
2  Simple Vector Regressor        15532.0           3795.0
3            Decision Tree        44000.0          11333.0
4  Random Forest Regressor        39767.0          11160.0


#Tüm parametrelerle
Lineer Reg. R2 Score 0.5857207050854021
Polynomial R2 Score 0.8871429857650682
SVM R2 Score 0.6287203839391853
Decision Tree R2 Score 1.0
Random Forest R2 Score 0.9497247261456644
                    Yöntem  10 Yıllık CEO  10 Yıllık Müdür
0                   Lineer        31997.0          21701.0
1               Polynomial        58661.0          22994.0
2  Simple Vector Regressor        17962.0           2316.0
3            Decision Tree        60000.0          12000.0
4  Random Forest Regressor        49850.0          11963.0

#Kıdem ve unvansırası ile
Lineer Reg. R2 Score 0.5596179274269741
Polynomial R2 Score 0.8452039043068785
SVM R2 Score 0.7273465023811729
Decision Tree R2 Score 1.0
Random Forest R2 Score 0.9657984751548029
                    Yöntem  10 Yıllık CEO  10 Yıllık Müdür
0                   Lineer        29654.0          19683.0
1               Polynomial        51996.0          21054.0
2  Simple Vector Regressor        15081.0           3217.0
3            Decision Tree        60000.0          12000.0
4  Random Forest Regressor        53710.0          11395.0


'''




