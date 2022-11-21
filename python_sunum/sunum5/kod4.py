'''
Tek mi çift mi programı

Girilen sayının tek mi çift mi olduğunu gösteren program

Kullanıcıdan bir sayı girmesi istenecek
Ondalık sayı girdiyse tam kısmı alınacak
Sayının 2ye bölümünden kalan bulunacak
Ekrana sayının çift veya tek olduğu yazılacak

'''

s=int(float(input('Bir sayı giriniz')))

if s % 2 == 0:
    print(s, "sayısı çift")
else:
    print(s, "sayısı tek")

input()