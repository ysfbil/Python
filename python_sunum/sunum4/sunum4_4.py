
def sayiBul():
    
    deger=int(input("1-10 arasında bir sayı giriniz:"))
    if deger<5:
        print("sayı 5ten küçük")
    elif deger==5:
        print("sayı 5tir")
    else:
        print("sayı 5ten büyük")
    print("Hoşçakalın")
    
    devam=input("Devam mı?(E/H)")
    if devam=="E": sayiBul()

sayiBul()

#input()