print("""
***************************************
ATM Makinesine Hoşgeldiniz.

İşlemlemler;

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Programdan çıkmak için 'q' ya basın.
***************************************
""")

bakiye = 1000

while True:
    islem = input("İşlemi seçiniz:")

    if(islem == "q"):
        print("Yine bekleriz")
        break
    elif(islem == "1"):
        print("Bakiyeniz {} tl'dir".format(bakiye))
    elif(islem == "2"):
        miktar = int(input("Miktarı giriniz: "))
        bakiye += miktar
    elif(islem == "3"):
        while True:
            miktar = input("Çekmek istediğiniz miktarı giriniz: ")
            if (miktar == "q"):
                print("Ana menüye dönülüyor...")
                break
            miktar = int(miktar)
            if(bakiye < miktar):
                print("Yetersiz bakiye. Lütfen tekrar deneyiniz.")
                continue
            bakiye -= miktar
            print(f"{miktar} TL çektiniz. Kalan bakiye: {bakiye} TL")
            break
    else:
        print("Geçersiz İşlem...")