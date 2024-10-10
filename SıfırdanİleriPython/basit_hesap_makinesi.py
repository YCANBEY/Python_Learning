print("""***********************
Hesap Makinesi Programı

İşlemler;

1. Toplama İşlemi

2 Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi
****************************
""")

a = int(input("İlk Sayıyı Giriniz:"))
b = int(input("İkinci Sayıyı Giriniz:"))

islem = input("İşlemi Giriniz:")

if(islem == "1"):
    print("{} + {} = {}".format(a,b,a+b))
elif(islem == "2"):
    print("{} - {} = {}".format(a,b,a-b))
elif(islem == "3"):
    print("{} * {} = {}".format(a,b,a*b))
elif(islem == "4"):
    print("{} / {} = {}".format(a,b,a/b))
else:
    print("Geçersiz işlem")