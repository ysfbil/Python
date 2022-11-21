import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

veriler = pd.read_csv('datas/odev_tenis.csv')
print(veriler)

windy = veriler.iloc[:, 3:4].apply(LabelEncoder().fit_transform)
play = veriler.iloc[:, 4:5].apply(LabelEncoder().fit_transform)
# print(play)
outlook = veriler.iloc[:, :1]
# print(outlook)
ohv = OneHotEncoder(categories='auto')
outlook = ohv.fit_transform(outlook).toarray()
# print(outlook)
temprature = veriler.iloc[:, 1:2]
humidity = veriler.iloc[:, 2:3]
'''
sc = StandardScaler()
humidity = pd.DataFrame(sc.fit_transform(humidity))
temprature =  pd.DataFrame(sc.fit_transform(temprature))
print(type(temprature))
'''
outlook = pd.DataFrame(data=outlook, index=range(14), columns=['overcast', 'rainy', 'sunny'])
veriTablosu = pd.concat([outlook, temprature, humidity, windy, play], axis=1)
# print(veriTablosu.iloc[:,-1:])
print(veriTablosu)
x_train, x_test, y_train, y_test = train_test_split(veriTablosu.iloc[:, :-1], veriTablosu['play'],
                                                    test_size=0.33, random_state=56)
lr = LinearRegression()
lr.fit(x_train, y_train)

y_pred = lr.predict(x_test)
sonuc = pd.DataFrame([y_pred, y_test])
print(sonuc)
