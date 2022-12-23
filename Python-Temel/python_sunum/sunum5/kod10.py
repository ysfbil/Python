karakter=input("Tekbir karakter giriniz:")

if karakter.isupper():
    m="büyük harf girdiniz"
elif karakter.islower():
    m="küçük harf girdiniz"
elif karakter.isdigit():
    m="sayı girdiniz"
else:
    m="sembol girdiniz"

print(m)

input()