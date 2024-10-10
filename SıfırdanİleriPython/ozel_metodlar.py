class Kitap():

    def __init__(self,isim,yazar,sayfa_sayısı,türü):

        print("İnit fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.türü = türü

    def __str__(self):

        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTürü: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.türü)

    def __len__(self):
        return self.sayfa_sayısı

kitap = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
print(kitap)
print("Sayfa sayısı:",len(kitap))

# Diğer özel metodlara bakmak için
#https://diveintopython3.net/special-method-names.html