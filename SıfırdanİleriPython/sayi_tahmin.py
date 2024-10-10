import random
import time

rastgele_sayi = random.randint(1,40)
tahmin_hakki = 7

while True:
    tahmin = int(input("Tahmininiz:"))

    if(tahmin < rastgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha büyük bir sayı giriniz.")
        tahmin_hakki -= 1
    elif(tahmin > rastgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha küçük bir sayı giriniz.")
        tahmin_hakki -= 1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print(f"Tebrikler sayınız {rastgele_sayi}")
        break
    if(tahmin_hakki == 0):
        print("Tahmin hakkınız bitti...")
        break