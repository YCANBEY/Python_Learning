# 1) dir - Yardım
# 2) help - Yardım (dir'in daha detaylısı)
# 3) enumarete - Numaralandırma
# 4) isistance - Doğrulama
# 5) pow - Üs alma
# 6) round - Yuvarlama
# 7) zip - Eşleştirme

# 1)
# print(dir(str))

# 2)
# print(help(str))

# 3)
# print(list(enumerate("Python")))
# for i, j in list(enumerate("Python")):
#     print(i, j)

# 4)
# print(isinstance("s",str))

# 5)
# print(pow(5,3))

# 6)
# print(round(22/7,3)) # 3 dediğimiz için virgülden sonra 3 basamağa kadar yuvarlar. Burada sonuç 3.143 gelir
# print(round(22/7))   # böyle yazarsak tam sayıya yuvarlar. Burada sonuç 3 gelir

# 7)
# indeksleri birbirine eşleştirir. Birisinde fazla indeks varsa,fazla olana eşleştirme yapmaz.
# isimler = ["Ahmet", "Ali", "Ayşe", "Mehmet", "Veli"]
# yaslar = [24,36,78,55]
#
# print(list(zip(isimler,yaslar))) # Bu durumda Veli'yi yazmadı.