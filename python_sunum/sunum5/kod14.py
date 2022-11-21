'''
girlien harfi sesli harf olup olmadığını gösteren program
'''

k=input("Bir harf giriniz")
k=k.lower()

if (k=="a" or k=="e" or k=="ı" or k=="i" or k=="o" or k=="ö" or k=="u" or
    k=="ü"):

    print(k, "bir sesli harftir")
else:
    print(k, "bir sessiz harftir")

input()