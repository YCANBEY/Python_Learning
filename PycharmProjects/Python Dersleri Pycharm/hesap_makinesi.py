def hesapMakinesi ():
     print("""
     İşlem liste;
     1) Toplama
     2) Çıkarma
     3) Bölme
     4) Çarpma
     """)

     islem = int(input("İşlem seçiniz: "))
     if islem != 5:
         ilkSayi = int(input("İlk sayıyı giriniz: "))
         ikinciSayi = int(input("İkinci sayıyı giriniz: "))

         if islem == 1:
             print("Toplama işleminin sonucu: ")
             return f"{ilkSayi} + {ikinciSayi} = {ilkSayi + ikinciSayi}"
         elif islem == 2:
             print("Çıkarma işleminin sonucu: ")
             return f"{ilkSayi} - {ikinciSayi} = {ilkSayi - ikinciSayi}"
         elif islem == 3:
             print("Bölme işleminin sonucu: ")
             return f"{ilkSayi} / {ikinciSayi} = {ilkSayi / ikinciSayi}"
         elif islem == 4:
             print("Çarpma işleminin sonucu: ")
             return f"{ilkSayi} * {ikinciSayi} = {ilkSayi * ikinciSayi}"
     else:
         return "Hatalı giriş yaptınız. "


islemHakki = 0
while islemHakki < 4:
    print(hesapMakinesi())
    islemHakki += 1
    print(f"Kalan işlem hakkınız {4 - islemHakki}")

