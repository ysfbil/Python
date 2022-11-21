# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 17:00:03 2022

@author: fizik
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
hamveri=pd.read_csv('datas/maaslar_yeni.csv')
veri=hamveri.drop(['Calisan ID','unvan'],axis=1)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
y=veri.iloc[:,-1]
x=veri.iloc[:,:-1]
lr=lr.fit(x,y)
y_p=lr.predict(x)
ud=x.iloc[:,:1]
print(hamveri.sort_values(by=['UnvanSeviyesi','maas']))
'''
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


x_test10=[[10,9,100],[7,9,100]] #ceo 10 ,mudur 7 100 puan almış 9 kıdemili müdür ve ceo maaşları
x_test10=pd.DataFrame(data=x_test10,columns=['UnvanSeviyesi','Kidem','Puan'])


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





