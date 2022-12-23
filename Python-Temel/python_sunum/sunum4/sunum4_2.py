

import time #zaman modülünü çağırıyoruz
vakit=time.localtime() #mevcut zamanı vakit değişkenine atıyoruz
saat=vakit.tm_hour #mevcut saati saat değişkenine veriyoruz
if saat<12: #saat değeri 12'den küçük mü
    print("Hayırlı sabahlar")   #Evet durumunda ekrana Hayırlı sabahlar yazdırıyoruz
if saat>=12: #saat değeri 12'den büyük mü
    print("Hayırlı günler") #Evet durumunda ekrana hayırlı günler yazdırıyoruz.


import time
vakit=time.localtime()
saat=vakit.tm_hour
print("Merhabalar...")
if saat<12:
    print("Hayırlı sabahlar")
else:
    print("Hayırlı günler")
print("Hoşçakalın...")
    

import time
vakit=time.localtime()
saat=vakit.tm_hour
print("Merhabalar...")
if saat<12:
    print("Sabah vakti")
elif saat<13:
    print("Öğlen vakti")
elif saat<17:
    print("İkindi vakti")
elif saat<22:
    print("Akşam vakti")
else:
    print("Gece vakti")
print("Hoşçakalın...")


input()