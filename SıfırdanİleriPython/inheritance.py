class Çalışan():

    def __init__(self,isim,maaş,departman):

        print("Çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.maaş = maaş
        self.departman = departman


    def bilgilerigöster(self):

        print("Çalışan sınıfının bilgileri.....")

        print("İsim :{}\nMaaş :{}\nDepartman :{}".format(self.isim,self.maaş,self.departman))

    def departman_değiştir(self,yeni_departman):

        self.departman = yeni_departman


class Yönetici(Çalışan):

    def zam_yap(self,zam_miktarı):

        self.maaş += zam_miktarı

yönetici = Yönetici("Yiğit",5000,"Bilişim")

yönetici.bilgilerigöster()

yönetici.departman_değiştir("İnsan Kaynakları")

yönetici.bilgilerigöster()

yönetici.zam_yap(3000)
yönetici.bilgilerigöster()