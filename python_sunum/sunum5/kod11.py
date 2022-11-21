'''
Aşağıdaki kodlar için olası çıktıları tahmin edelim
'''

deger=True

if not deger:
    print("1. Şart sağlanıyor")
else:
    print("1. Şart sağlanmıyor!")


# and=ve kullanımı

m,n,p=9,7,5

if (m>=n and m>=p):
    print("2. Şart sağlanıyor")
else:
    print("2. Şart sağlanmıyor!")

    

# and=ve ile değil=not kullanımı

if m>=n and not (p>m):
    print("3. şart sağlanıyor")
else:
    print("3. Şart sağlanmıyor!")

# or=veya kullanımı

if (m>n or m>p):
    print("4. şart sağlanıyor")
else:
    print("4. Şart sağlanmıyor!")

# not=değil ile or=veya kullanımı

if not (m>=n or m>=p):
    print("5. şart sağlanıyor")
else:
    print("5. Şart sağlanmıyor!")

input()