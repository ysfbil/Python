'''
Girilen sayı hem 2 ile hem de 3 ile tam 
bölünebiliyorsa "2 ve 3'ün katı", sadece 2 ile 
bölünebiliyorsa "2'nin katı”, sadece 3 ile 
bölünebiliyorsa "3'ün katı", ne 2'ye ne de 3'e 
bölünmüyorsa "2 veya 3'ün katı değil” 
mesajı veren program
'''

s=int(input("Bir sayı giriniz"))

if s%2==0:
    m="Sadece 2nin katı"
    if s%3==0:
        m="2 ve 3ün katı"
elif s%3==0:
    m="Sadece 3ün katı"
else:
    m="Ne 2 ne de 3ün katı"

print(m)

input()