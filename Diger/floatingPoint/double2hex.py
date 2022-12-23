import math



onalt = "40F40000" # input("Lütfen HEX sayı giriniz: ")

print("HEX sayı=",onalt);

onlu = int(onalt,16)
ikili=bin(onlu)[2:]
if (len(ikili)<32): #sayının 32 bit olması garantiliyoruz
    while (len(ikili)!=32):
        ikili='0'+ikili
        
print ("İkili karşılığı", ikili)
#print ("Onlu karşılığı",onlu)

S=ikili[0:1]
print("İşaret biti",S)

E=ikili[1:9]
print("Exponent=",E)

M=ikili[9:]
print("Mantissa=",M)

E10=int(E,2)
print("Exponent10=",E10)

n=E10-127
print("n=",n)
tam='1'+M[:n]
onda=M[n:]
print("İkili float=",tam+'.'+onda)
tam10=int(tam,2)

if (S=='1'):
    tam10 *=-1
print("Float tam onlu=",tam10)

onda10=0
i=1

for b in onda:
    onda10+=int(b)*2**(-i)
    i=i+1

print("Float ondalık onlu=",onda10)

if (S=='1'):
    onda10 *=-1

sonuc=tam10+onda10
print("Sonuç ondalıklı sayı=",sonuc)
# Print the resultant string




