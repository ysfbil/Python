def mesaj():
	print('selam')
	print('yusuf')
	
def kare(a):
	return a**2
	
def tamad(isim,soyisim):
	return isim+" "+soyisim

mesaj()
s=int(input('sayı giriniz'))
print(kare(s))

a=input('ad:')
b=input('soyad:')
print(tamad(a,b))