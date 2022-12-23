a=int(input("1. not: "))
b=int(input("2. not: "))
c=int(input("3. not: "))

if (a<0 or a>100 or b<0 or b>100 or c<0 or c>100):
    print("Hatalı not girişi")
else:
    ort=(a+b+c)/3
    print("Ortalamanız:",ort)
    
    if ort>=45:
        print("Geçtiniz")
    else:
        print("Kaldınız")
        
input()