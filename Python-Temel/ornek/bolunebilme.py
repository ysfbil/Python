a="61695423430387171270149468333085552739906279301544935796455193731679110572412922144898160566417122627982381681162907648552057245042404233840508137904250497"

print("Varsayılan sayı: ",a)
say=input("Bölünebilirliği kontrol edilecek sayıyı giriniz. Varsayılan sayı için boş geçiniz.\nSayı:")

if (say.strip()!=""): a=say
    
i=[1,3,2,-1,-3,-2]
t=0
k=0
#7 ile bölünebilme

for s in reversed(a):
   t+=int(s)*i[k]
   if k<5:
       k+=1
   else:
       k=0
if t<0:
    while t<0:
        t+=7

print("7 ile bölümden kalan : ",t%7, " \n7'ye bölünme formül sonucu: ", t)
print("1000000 bölenine kadar bölünebilme kontrol ediyor bekleyiniz!")
    

#1000000'e kadar bölünebilme kontrolu

ia=int(a)
sonuc=False
liste=[]

for r in range(2,1000000):
    if ia%r==0:
        sonuc=True
        liste.append(r)
        

if sonuc :
    for l in liste:
        print(l," sayısına tam bölünebiliyor.")
else:
    print(r," e kadar tam bölünemedi")


input()
