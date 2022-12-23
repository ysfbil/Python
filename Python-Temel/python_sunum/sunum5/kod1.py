'''
Yıllık Gelir kullacıya sorup
150bin veya altı ise %25
150bin-300bin arasında ise %30
300bin-600bin arasında ise %35
600bin üzerinde ise %40 vergi uygulayalım.
ve kullanıcıya ödeyeceği vergi tutarını gösterelim.
'''

ygelir=int(input("Yıllık gelirinizi yazınız:"))

if ygelir<=150000:
    vergi=ygelir*0.25
elif ygelir<=300000:
    vergi=ygelir*0.30
elif ygelir<=600000:
    vergi=ygelir*0.35
else:
    vergi=ygelir*0.4

print("Ödemeniz gereken vergi=",vergi)

input()
