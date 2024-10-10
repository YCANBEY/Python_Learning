print("""
************************************************
Bir sayının kendi hariç bölenlerinin toplamı
kendine eşitse bu sayıya "mükemmel sayı" denir.

Programdan çıkmak için q'ya basınız.
""")

while True:
    toplam = 0
    sayı = input("Sayı giriniz veya programdan çıkmak için q'ya basınız")
    if (sayı == "q"):
        print("Programdan çıkılıyor...")
        break
    else:
        sayı = int(sayı)
        liste = list()
        for i in range(1,sayı):
            if(sayı % i == 0):
                toplam += i
        if(toplam == sayı):
            print(f"{sayı} mükemmel sayıdır.")
        else:
            print(f"{sayı} mükemmel sayı değildir.")