"""
Bir sayı eğer 4 basamaklı ise ve oluşturulan rakamlardan
herbirinin 4.kuvvetinin toplamı(3 basamaklı sayılar için
3. kuvveti) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
"""

sayı = input("Sayı: ")
basamak_sayisi = len(sayı)
sayi_liste = list()

for i in sayı:
    sayi_liste.append(int(i))
toplam = 0
for rakam in sayi_liste:
    toplam += rakam ** basamak_sayisi
sayı = int(sayı)
if(toplam == sayı):
    print(f"{sayı} bir armstrong sayısıdır.")
else:
    print(f"{sayı} bir armstrong sayısı değildir.")