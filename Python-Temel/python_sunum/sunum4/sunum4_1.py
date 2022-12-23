import time
vakit=time.localtime()
saat=time.strftime("%H",vakit) #saati verir %M: ay %S:saniye
print("Saat: ",saat)

print("Saat: ", vakit.tm_hour) #diğer zaman bileşenleri tm_year, tm_mon, tm_mday, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst
print(type(vakit.tm_hour))

import datetime
now = datetime.datetime.now()
print (now.year, now.month, now.day, now.hour, now.minute, now.second)
# 2015 5 6 8 53 40
input()