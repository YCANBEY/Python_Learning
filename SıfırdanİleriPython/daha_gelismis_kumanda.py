import random
import time


class Kumanda():

    def __init__(self, tv_durum="Kapalı", tv_ses=0,
                 kanal_listesi=["Trt"], kanal="Trt",
                 favori_kanal=[]):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        self.favori_kanal = favori_kanal

    def tv_ac(self):

        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if (self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon kapanıyor...")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):

        if (self.tv_durum == "Kapalı"):
            print("Televizyon kapalı, bu işlemi gerçekleştiremezsiniz!")
            return

        while True:

            cevap = input("Sesi Azalt: '<'\nSesi Arttır: '>'\nÇıkış: 'çıkış'")

            if (cevap == "<"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses: ", self.tv_ses)
                elif (cevap == ">"):
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)
            else:
                print("Ses güncellendi:", self.tv_ses)
                break

    def kanal_ekle(self, kanal_ismi):

        if (self.tv_durum == "Kapalı"):
            print("Televizyon kapalı, bu işlemi gerçekleştiremezsiniz!")
            return

        kanallar = kanal_ismi.split(",")

        print("Kanallar ekleniyor")
        time.sleep(1)

        for kanal in kanallar:
            kanal = kanal.strip()  # Boşlukları temizler
            if kanal not in self.kanal_listesi:
                self.kanal_listesi.append(kanal)
                print(f"{kanal} eklendi...")
            else:
                print(f"{kanal} zaten kanal listeniz mevcut.")

    def rastgele_kanal(self):

        if (self.tv_durum == "Kapalı"):
            print("Televizyon kapalı, bu işlemi gerçekleştiremezsiniz!")
            return

        rastgele = random.randint(0, len(self.kanal_listesi) - 1)

        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki Kanal:", self.kanal)

    def __len__(self):

        return len(self.kanal_listesi)

    def favori(self, favori_kanallar):

        if (self.tv_durum == "Kapalı"):
            print("Televizyon kapalı, bu işlemi gerçekleştiremezsiniz!")
            return

        print("Favorilere geçildi.")
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.favori_kanal.append(favori_kanallar)

    def favori_kanal_ekle(self, favori_kanal_ismi):
        if (self.tv_durum == "Kapalı"):
            print("Televizyon kapalı, bu işlemi gerçekleştiremezsiniz!")
            return
        favori_kanallar = favori_kanal_ismi.split(",")
        for kanal in favori_kanallar:
            kanal = kanal.strip()  # gereksiz boşlukları temizler
            if kanal not in self.favori_kanal:
                print(f"{kanal} favori kanallarına ekleniyor")
                self.favori_kanal.append(kanal)
            else:
                print(f"{kanal} zaten favori kanallarınızda mevcut")
        print("Favori kanallar eklendi...")

    def favori_rastgele_kanal(self):
        if (self.tv_durum == "Kapalı"):
            print("Televizyon kapalı, bu işlemi gerçekleştiremezsiniz!")
            return
        if (len(self.favori_kanal) == 0):
            print("Favori kanal listeniz boş!")
            return
        rastgele = random.randint(0, len(self.favori_kanal_ismi) - 1)
        self.kanal = self.favori_kanal[rastgele]
        print("Şu anki favori kanal:", self.kanal)

    def __str__(self):

        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal:{}\nFavori Kanallar: {}".format(
            self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal, self.favori_kanal
        )


kumanda = Kumanda()


class İşlemler(Kumanda):

    def __init__(self, kumanda):
        self.kumanda = kumanda

    def menü(self):
        while True:
            print("""
            Televizyon Uygulaması

            1. Tv Aç
            2. Tv Kapat
            3. Ses Ayarları
            4. Kanal Ekle
            5. Kanal Sayısını Öğrenme
            6. Rastgele Kanala Geçme
            7. Televizyon Bilgileri
            8. Favori Kanallara Geçme
            9. Favori Kanal Menüsü

            Çıkmak için 'q' ya basın
            """)

            işlem = input("Bir İşlem seçiniz: ")

            if (işlem == "q"):
                print("Programdan çıkılıyor...")
                break
            elif (işlem == "1"):
                self.kumanda.tv_ac()
            elif (işlem == "2"):
                self.kumanda.tv_kapat()
            elif (işlem == "3"):
                self.kumanda.ses_ayarları()
            elif (işlem == "4"):
                kanal_isim = input("Eklenecek kanal ismini girin:")
                self.kumanda.kanal_ekle(kanal_isim)
            elif (işlem == "5"):
                print("Kanal sayısı:", len(self.kumanda))
            elif (işlem == "6"):
                self.kumanda.rastgele_kanal()
            elif (işlem == "7"):
                print(self.kumanda)
            elif (işlem == "8"):
                favori_kanal = input("Favori kanal ismini girin: ")
                self.kumanda.favori(favori_kanal)
            elif (işlem == "9"):
                self.favori_menü()
            else:
                print("Geçersiz İşlem")

    def favori_menü(self):

        while True:
            print("""
            Favori Kanallar Menüsü

            1. Favori Kanallara Kanal Ekle
            2. Rastgele Favori Kanala Geç
            3. Favori Kanal Listesini Görüntüle
            4. Ana Menüye Dön
            """)

            işlem = input("Bir İşlem Seçiniz:")

            if (işlem == "1"):
                favori_kanal = input("Eklenecek favori kanal ismini veya isimlerini ',' koyarak giriniz:")
                self.kumanda.favori_kanal_ekle(favori_kanal)
            elif (işlem == "2"):
                self.kumanda.favori_rastgele_kanal()
            elif (işlem == "3"):
                print("Favori kanal listesi:", self.kumanda.favori_kanal)
            elif (işlem == "4"):
                break
            else:
                print("Geçersiz İşlem!")


kumanda = Kumanda()
işlemler = İşlemler(kumanda)
işlemler.menü()