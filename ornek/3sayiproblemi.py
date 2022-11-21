say1=float(input("1. sayı: "))
say2=float(input("2. sayı: "))
say3=float(input("3. sayı: "))
enbuyuk=say3

if say1>say2:
	if say1>say3:
		enbuyuk=say1
else:
	if say2>say3:
		enbuyuk=say2
	
print('En büyük',enbuyuk)

input()
