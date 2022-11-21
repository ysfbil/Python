def belge(notlar):
	ort=0
	s=0
	
	for n in notlar:
		ort+=n
		s+=1
	ort=ort/s
	
	if ort>84.99:
		return  'Takdir Ort:'+str(ort)
	elif ort>=70:
		return 'Teşekkür Ort:'+str(ort)
	else:
		return 'Belge alamadınız Ort:'+str(ort)
		
notum=[]
g=0

print('Notlarınızı giriniz/Girişi tamamlamak için -1 giriniz.')
while(g>-1):
	g=int(input('Not:'))
	if g>-1:
		 notum.append(g)
		
print(belge(notum))
input()