say1=int(input("1. sayı: "))
say2=int(input("1. sayı: "))
say3=int(input("1. sayı: "))
enbuyuk=say1
orta=say2
enkucuk=say3

if say1>say2:
	if say1>say3:
		enbuyuk=say1
		if say3>say2:
			orta=say3
			enkucuk=say2
		else:
			enkucuk=say3
	else:
		enbuyuk=say3
		orta=say1
		enkucuk=say2
else:
	if say2>say3:
		enbuyuk=say2
		if say3>say1:
			orta=say3
			enkucuk=say1
		else:
			enkucuk=say3
			orta=say1
	else:
		enbuyuk=say3
		enkucuk=say1
	
print(enbuyuk,'>',orta,'>',enkucuk)

input()
