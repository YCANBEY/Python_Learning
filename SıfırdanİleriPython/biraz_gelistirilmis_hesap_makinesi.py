import math

"""
Gelişmiş hesap makinesi
"""

print("""
*********************************
Toplama için 1:
Çıkarma için 2:
Çarpma için 3:
Bölme için 4:
Yüzde hesaplamak için 5:
Karakök için 6:
Küpkök için 7:
Faktöriyel hesabı için 8:
Programdan çıkmak için q:
*********************************
""")

while True:
    islem = input("İşlem tercihinizi giriniz:")

    if(islem == "q"):
        print("Programdan çıkılıyor...")
        break

    if(islem == "1"):
        sayı1 = int(input("Birinci sayıyı giriniz:"))
        sayı2 = int(input("İkinci sayıyı giriniz:"))

        toplam = sayı1 + sayı2
        print(f"{sayı1} + {sayı2} = {toplam}")
    elif(islem == "2"):
        sayı1 = int(input("Birinci sayıyı giriniz:"))
        sayı2 = int(input("İkinci sayıyı giriniz:"))

        fark = sayı1 - sayı2
        print(f"{sayı1} - {sayı2} = {fark}")
    elif(islem == "3"):
        sayı1 = int(input("Birinci sayıyı giriniz:"))
        sayı2 = int(input("İkinci sayıyı giriniz:"))

        carpım = sayı1 * sayı2
        print(f"{sayı1} * {sayı2} = {carpım}")

    elif(islem == "4"):
        sayı1 = int(input("Birinci sayıyı giriniz:"))
        sayı2 = int(input("İkinci sayıyı giriniz:"))

        bolum = sayı1 / sayı2
        print(f"{sayı1} / {sayı2} = {bolum}")

    elif(islem == "5"):
        sayı = int(input("Sayıyı giriniz:"))
        yuzde = int(input("Yüzdeyi giriniz:"))

        sonuc = (sayı * yuzde) / 100
        print(f"{sayı} yüzdesi {sonuc}")

    elif(islem == "6"):
        sayı = int(input("Sayıyı giriniz:"))

        karekok = math.sqrt(sayı)
        print(f"{sayı} karekökü {karekok}")
    elif(islem == "7"):
        sayı = int(input("Sayıyı giriniz:"))
        kupkok = sayı ** (1/3)
        print(f"{sayı} küpkökü {kupkok}")

    elif(islem == "8"):
        sayı = int(input("Sayı giriniz:"))

        faktoriyel = math.factorial(sayı)
        print(f"{sayı}! = {faktoriyel}")