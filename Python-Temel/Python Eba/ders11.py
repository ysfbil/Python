from time import * #clock yazarsak sadece o kısmı import etmiş oluşuruz. import time ile de tümü import edilebilir

t1=perf_counter()
input('Adınız')
t2=perf_counter()
print((t2-t1),'kadar süre geçti')
input()