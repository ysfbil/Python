'''
Rastgele sayı üretip üretilen sayının pozitif veya negatifliğini
kontrol edelim
'''

import random

s=random.randrange(-5,5)

if s>0:
    print(s, "sayısı pozitiftir")
else:
    print(s,"sayısı negatiftir")

input()