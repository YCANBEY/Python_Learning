# lambda - isimsiz fonksiyonlar oluşturmamızı sağlar
# deften farkı, tek seferlik fonksiyon olması

# def karesiAl(x):
#     return x ** 2
# print(f"def karesini al çalıştı {karesiAl(5)}")
#
# a = lambda x : x ** 2
# print(f"lambda karesini al çalıştı {a(5)}")
#
# def kupAl(x):
#     return x ** 3
# print(f"def küp al çalıştı {kupAl(5)}")
#
# b = lambda x : x ** 3
# print(f"lambda küp al çalıştı {b(5)}")
#
# c = lambda *args : sum(args) / len(args)
# print(f"ortalama : {c(3, 6, 9)}")

# MAP

# liste1 = [2, 3, 6, 5, 69]
#
# def karesiniAl(x):
#     return x ** 2
#
# liste2 = []
#
# for i in liste1:
#     liste2.append(karesiniAl(i))
#
# print(liste2)
#
# # Peki bunu map fonksiyonu ile nasıl yaparız ?
# # 1) map(a,b) ; a kısmı fonksiyonumuzdur, b kısmı ise veri kısmıdır.
# # Bu veri kısmı üzerinde gezilebilecek bir veri tipi olmalı. Örneğin liste
#
# print(list(map(karesiniAl,liste1)))
#
# a = list(map(lambda x : x ** 2, liste1))
# print(a)

# FİLTER

# filter boolean değer döner
# filter(fonksiyon,üzerinde gezebileceğimiz bir veri tipi) üzerinde gezilenler tuple,list falan
# Parantezle birlikte fonksiyonu çağırdığımız zaman bu fonksiyonu çalıştırmış oluyoruz.
# Yani şöyle yazarsak ; filter(fonksiyon(),list)
# Parantezsiz iken fonksiyonu sadece parametre olarak veririz.

liste = [*range (1,100,3)] # 1'den 100'e kadar 3'erli giderek bir liste oluştur. 1'i al 3 atla yani 4'ü al 3 atla 7'yi al şeklinde.

print(liste)
def tekÇift(x):
    if x %2 == 0:
        return x
    else:
        None

print(list(filter(tekÇift , liste)))

# şimdi lambda ile tek sayıları yazalım

print(list(filter(lambda x : x %2 == 1,liste)))