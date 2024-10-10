
class Çalışan():

    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgilerigöster(self):
        print("Çalışan sınıfının bilgileri....")

        print("İsim : {}\nMaaş : {}\nDepartman : {}".format(self.isim,self.maaş,self.departman))

    def departman_değiştir(self,yeni_departman):
        self.departman = yeni_departman

class Yönetici(Çalışan):
    def __init__(self,isim,maaş,departman,kişi_sayısı):

        #çalışan sınıfındaki isim maaş departman bilgilerini
        #kullanmak için super kullanırız
        super().__init__(isim,maaş,departman)


        print("Yönetici sınıfının init fonksiyonu")

        self.kişi_sayısı = kişi_sayısı

    def bilgilerigöster(self):
        print("Yönetici sınıfının bilgileri...")

        print("İsim : {}\nMaaş : {}\nDepartman : {}\nSorumlu Kişi Sayısı: {}".format(self.isim, self.maaş, self.departman,self.kişi_sayısı))

    def zam_yap(self,zam_miktarı):
        self.maaş += zam_miktarı

yönetici = Yönetici("Ali",3500,"Bilişim",10)
yönetici.bilgilerigöster()