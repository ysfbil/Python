'''
Girilen 100lük sistemdeki notu 5lik sisteme çeviren program

not  0-24  arası 0 Etksiz
not 25-44  arası 1 Geçmez
not 45-54  arası 2 Geçer
not 55-69  arası 3 Orta
not 70-84  arası 4 İyi
not 85-100 arası 5 Pekiyi

kullanıcıdan ders notunu girmesini isteyecek
yukarıdaki çizelgeye göre kullanıcının 5lik notunu ve derecesini ekrana yazcak
not 0dan küçük veya 100den büyük ise uyarı verecek
'''

p=int(input('100lük sistemdeki puanınızı giriniz'))

if p<0:
    m="Puan 0dan küçük olamaz"
elif p<=24:
    m="not=0, Etkisiz"
elif p<=44:
    m="not 1 Geçmez"
elif p<=54:
    m="not 2 Geçer"
elif p<=69:
    m="not 3 orta"
elif p<=84:
    m="not 4 iyi"
elif p<=100:
    m="not 5 pekiyi"
else:
    m="notunuz 100den büyük olamaz"

print(m)

input()