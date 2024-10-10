print("""
*****************************
Kullanıcı Girişi Programı
*****************************
""")

sys_kullanıcı_adı = "vveli"

sys_parola = "12345"

giris_hakkı = 3
while True:
    kullanıcı_adı = input("Kullanıcı Adı: ")
    parola = input("Parola: ")

    if (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı Adı Hatalı...")
        giris_hakkı -=1
    elif(kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Parola Hatalı...")
        giris_hakkı -=1
    elif(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı...")
        giris_hakkı -=1
    else:
        print("Sisteme Başarıyla Giriş Yapıldı....")
        break
    if(giris_hakkı == 0):
        print("Giriş Hakkınız Bitti...")
        break