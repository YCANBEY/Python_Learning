#--------------------------------------- FONKSİYONLAR -------------------------------------------------
# Formül yazılımını kolaylaştıran kod blokları.
# Def anahtar kelimesiyle yazıyoruz.

def topla(sayi1 = 5,sayi2 = 10): # varsayılan öylesine bir değer atadık,
    print(sayi1+sayi2)
# topla()                           # yani toplaya herhangi bir parametre girmezsek bu sayıları kullanıcak.
# topla(25,50)                      # Parametre girersek girdiğimiz parametreleri toplayacak

# def selamla(metin,isim):
#     print(metin+isim)
# selamla("Merhaba ", "Ali")           # Burada önce ali'yi yazsaydık ali merhaba çıktısını alırdık
# selamla("Ali ", "Merhaba")           # Yani şu şekilde ; Çünkü hangisinin hangi parametre olduğunu bilmiyor
# selamla(isim="ali",metin="Merhaba ") # Bunun önüne geçmek için parametreleri belirtebiliriz.

# return (döndürmek) print(yazdırmak)

# def carp(sayi1 = 5, sayi2 = 10): # varsayılan değer atadık.
#     print(sayi1 * sayi2)
#
# x = carp(5,5)
# print(x) # none şeklinde bir uyarı alırız çünkü belleğe kaydedilmez print sadece küçük yazılar mesajlar için
#          # detaylı işlemlerde return kullanırız onu da altta yapalım

def carp(sayi1 = 5, sayi2 = 10):
    return(sayi1 * sayi2) # bu şekilde yaparsak none almayız çünkü belleğe kaydeder, return de paranteze gerek yok.
                          # istersek return sayi1 * sayi2 şeklinde yazabiliriz
# x = carp(5,5)
# print(x)

# f string içinde parametre kullanmak için süslü parantez kullanırız !!

def ortalama(listeGir):
    return f"Girilen listenin ortalaması: {sum(listeGir)/len(listeGir)}"
#print(ortalama([1,2,3,4,5]))

# metinlerin sadece baş harflerini büyük yapan metot capitalize()

def basHarfBuyukYap(metin):
    return metin.capitalize()
# print(basHarfBuyukYap("KORKMA, SÖNMEZ BU ŞAFAKLARDA YÜZEN ALSANCAK"))

# metinlerdeki kelimelerin baş harflerini büyük yapmak için title()
def kelimeBasHarfBuyukYap(metin):
    return metin.title()
# print(kelimeBasHarfBuyukYap("KORKMA, SÖNMEZ BU ŞAFAKLARDA YÜZEN ALSANCAK"))


# args(argümanlar) - kwargs(anahtar kelime argümanları)
# args yazımı : *args , kwargs yazımı : **kwargs

def toplam(*args): # sınırsız argüman
    return sum(args)
# print(toplam(1,2,5,6,12,35,65,89,25,36))

def anahtarKelime(**kwargs):
    for i in kwargs:
        print(i)

anahtarKelime(ahmet = 50, ali = 45, ayse = 30)
